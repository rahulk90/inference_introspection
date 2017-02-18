import os,time,sys
sys.path.append('../')
import numpy as np
from datasets.load import loadDataset
from optvaedatasets.load import loadDataset as loadDataset_OVAE
from optvaeutils.parse_args_dan import params 
from optvaeutils.vocab_utils import reformatDataset
from utils.misc import removeIfExists,createIfAbsent,mapPrint,saveHDF5,displayTime,getLowestError, loadHDF5
from sklearn.feature_extraction.text import TfidfTransformer

dataset = params['dataset']
params['savedir']+='-'+dataset+'-'+params['opt_type']
createIfAbsent(params['savedir'])
print 'Loading: ',dataset 
dataset = loadDataset_OVAE(dataset)

#Load datasets that you're using to 
dataset_wvecs = params['dataset_wvecs']
print 'Loading: ',dataset_wvecs 
dataset_wvecs = loadDataset_OVAE(dataset_wvecs)

reformatDataset(dataset, dataset_wvecs)

#Load Jacobian vectors
print 'Loading Jacobian'
saved_jacob   = loadHDF5(params['jacobian_location'])
jacobian      = saved_jacob[params['jacobian_type']]

for prefix in ['train','valid','test']:
    for dnum, idxvec, maskvec in zip(np.arange(dataset[prefix+'_x'].shape[0]),dataset[prefix+'_x'], dataset[prefix+'_mask']):
        idxlist = idxvec[:int(maskvec.sum())].astype(int).tolist() 
        for idx in idxlist:
            if np.linalg.norm(jacobian[idx]) > 50:
                print 'Bad! Setting mask to 0: ',prefix,dnum,idx,dataset_wvecs['vocabulary'][idx]
                iloc  = idxlist.index(idx)
                dataset[prefix+'_mask'][dnum,iloc] = 0.
attrs         = {}
attrs['jacobian_th'] = jacobian

assert jacobian.shape[0] == len(dataset_wvecs['vocabulary']),'shapes dont match up'
params['dim_input']      = jacobian.shape[1]
params['dim_output']     = len(np.unique(dataset['train_y']))

#Store dataset parameters into params 
mapPrint('Options: ',params)
#Setup VAE DAN (or reload from existing savefile)
start_time = time.time()
from optvaemodels.dan import DAN 
from optvaemodels.dan import learn
from optvaemodels.dan import evaluateAcc


import ipdb;ipdb.set_trace()
displayTime('import DAN',start_time, time.time())
vae    = None
#Remove from params
start_time = time.time()
removeIfExists('./NOSUCHFILE')
reloadFile = params.pop('reloadFile')
if os.path.exists(reloadFile):
    pfile=params.pop('paramFile')
    assert os.path.exists(pfile),pfile+' not found. Need paramfile'
    print 'Reloading trained model from : ',reloadFile
    print 'Assuming ',pfile,' corresponds to model'
    model = DAN(params, paramFile = pfile, reloadFile = reloadFile, additional_attrs = attrs)
else:
    pfile= params['savedir']+'/'+params['unique_id']+'-config.pkl'
    print 'Training model from scratch. Parameters in: ',pfile
    model = DAN(params, paramFile = pfile, additional_attrs = attrs)
displayTime('Building vae',start_time, time.time())

savef      = os.path.join(params['savedir'],params['unique_id']) 
start_time = time.time()

#Setup jacobian
savedata   = learn( model,  dataset     = dataset['train_x'],
                            mask        = dataset['train_mask'],
                            labels      = dataset['train_y'],
                            epoch_start = 0 , 
                            epoch_end   = params['epochs'], 
                            batch_size  = params['batch_size'],
                            savefreq    = params['savefreq'],
                            savefile    = savef,
                            dataset_eval= dataset['valid_x'],
                            mask_eval   = dataset['valid_mask'],
                            labels_eval = dataset['valid_y']
                            )
displayTime('Running DAN',start_time, time.time())
# Work w/ the best model thus far
epochMin, valMin, idxMin = getLowestError(savedata['valid_acc'])
reloadFile               = pfile.replace('-config.pkl','')+'-EP'+str(int(epochMin))+'-params.npz'
print 'Loading from : ',reloadFile
params['validate_only']  = True
bestDAN                  = DAN(params, paramFile = pfile, reloadFile = reloadFile, additional_attrs = attrs)
test_nll, test_acc, test_confusion_mat  = evaluateAcc(bestDAN, dataset['test_x'], dataset['test_mask'], dataset['test_y'], batch_size = params['batch_size'])
savedata['test_nll']           = test_nll
savedata['test_acc']           = test_acc
savedata['test_confusion_mat'] = test_confusion_mat
saveHDF5(savef+'-final.h5', savedata)
#import ipdb; ipdb.set_trace()