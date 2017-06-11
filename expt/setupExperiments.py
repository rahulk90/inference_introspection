""" Commands to reproduce experimental results """
from collections import OrderedDict
import sys

expt_type = 'rcv2_tfidf'
valid_expts= set(['20newsgroups_norm','20newsgroups_tfidf','20newsgroups_tfidf_qdrop','rcv2_norm','rcv2_tfidf','rcv2_q_vary','rcv2_tfidf_qdrop','rcv2_p_fixed','rcv2_p_fixed_random',
    'wikicorp','wikicorp_sparsity','wikicorp-large','wikicorp_evaluate','wikicorp_evaluate'])

print 'Valid Expts: ',','.join(list(valid_expts))
print 'Default: ',expt_type
if len(sys.argv)>=2:
    expt_type = sys.argv[-1].strip()
    if expt_type not in valid_expts:
        raise ValueError,(expt_type+' not a valid experiment')
print 'Selected: ',expt_type,'\n'

expt_runs              = OrderedDict() 
gpu_0_half = 'THEANO_FLAGS="compiledir_format=gpu0,lib.cnmem=0.45,scan.allow_gc=False"'
gpu_0_full = 'THEANO_FLAGS="compiledir_format=gpu0,lib.cnmem=0.95,scan.allow_gc=False"'
gpu_1_half = 'THEANO_FLAGS="compiledir_format=gpu1,lib.cnmem=0.45,scan.allow_gc=False"'
gpu_1_full = 'THEANO_FLAGS="compiledir_format=gpu1,lib.cnmem=0.95,scan.allow_gc=False"'
gpu_2_half = 'THEANO_FLAGS="compiledir_format=gpu2,lib.cnmem=0.45,scan.allow_gc=False"'
gpu_2_full = 'THEANO_FLAGS="compiledir_format=gpu2,lib.cnmem=0.95,scan.allow_gc=False"'
gpu_3_half = 'THEANO_FLAGS="compiledir_format=gpu3,lib.cnmem=0.45,scan.allow_gc=False"'
gpu_3_full = 'THEANO_FLAGS="compiledir_format=gpu3,lib.cnmem=0.95,scan.allow_gc=False"'

"""
Experiments on 20newsgroups
June 11- Rerun
"""
expt_runs['20newsgroups_norm'] = OrderedDict()
expt_runs['20newsgroups_norm']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -nl relu -otype none -pl 2 -ns 100 -ep 400'
expt_runs['20newsgroups_norm']['2_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -nl relu -otype finopt -pl 2 -ns 100 -ep 400'
expt_runs['20newsgroups_norm']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -nl relu -otype none -pl 0 -ns 100 -ep 400'
expt_runs['20newsgroups_norm']['0_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -nl relu -otype finopt -pl 0 -ns 100 -ep 400'

expt_runs['20newsgroups_tfidf'] = OrderedDict()
expt_runs['20newsgroups_tfidf']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 400'
expt_runs['20newsgroups_tfidf']['2_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 400'
expt_runs['20newsgroups_tfidf']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 400' 
expt_runs['20newsgroups_tfidf']['0_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype finopt -pl 0 -ns 100 -ep 400'

expt_runs['20newsgroups_tfidf_qdrop'] = OrderedDict()
expt_runs['20newsgroups_tfidf_qdrop']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 400 -idrop 0.5'
expt_runs['20newsgroups_tfidf_qdrop']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset 20newsgroups -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 400 -idrop 0.5' 

"""
Experiments on RCV2
"""
expt_runs['rcv2_norm'] = OrderedDict()
expt_runs['rcv2_norm']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -nl relu -otype none -pl 2 -ns 100 -ep 200'
expt_runs['rcv2_norm']['2_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -nl relu -otype finopt -pl 2 -ns 100 -ep 200'
expt_runs['rcv2_norm']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -nl relu -otype none -pl 0 -ns 100 -ep 200'
expt_runs['rcv2_norm']['0_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -nl relu -otype finopt -pl 0 -ns 100 -ep 200'

expt_runs['rcv2_tfidf'] = OrderedDict()
expt_runs['rcv2_tfidf']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200'
expt_runs['rcv2_tfidf']['2_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200'
expt_runs['rcv2_tfidf']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 200' 
expt_runs['rcv2_tfidf']['0_finopt'] = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 0 -ns 100 -ep 200'
expt_runs['rcv2_tfidf']['2-ar10k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -ar 10000'
expt_runs['rcv2_tfidf']['0-ar10k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 200 -ar 10000'
expt_runs['rcv2_tfidf']['2-ar50k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -ar 50000'
expt_runs['rcv2_tfidf']['0-ar50k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 200 -ar 50000'
expt_runs['rcv2_tfidf']['2-ar100k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -ar 100000'
expt_runs['rcv2_tfidf']['0-ar100k']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 200 -ar 100000'

expt_runs['rcv2_tfidf_qdrop'] = OrderedDict()
expt_runs['rcv2_tfidf_qdrop']['2_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -idrop 0.5'
expt_runs['rcv2_tfidf_qdrop']['0_none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 100 -ep 200 -idrop 0.5' 

"""
Run some experiments where you reload
"""
chkpt = {}
QVARYDIR = './results_qvary/chkpt-rcv2-finopt/'
chkpt['3-400-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-400-ds-100-pl-2-ql-3-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'
chkpt['2-400-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-400-ds-100-pl-2-ql-2-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'
chkpt['1-400-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-400-ds-100-pl-2-ql-1-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'
chkpt['3-100-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-100-ds-100-pl-2-ql-3-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'
chkpt['2-100-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-100-ds-100-pl-2-ql-2-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'
chkpt['1-100-p_fixed'] = QVARYDIR+'VAE_lr-8_0e-04-ph-400-qh-100-ds-100-pl-2-ql-1-nl-relu-bs-500-ep-200-plr-1_0e-02-ar-0-otype-finopt-ns-100-om-adam-etype-mlp-ll-mult-itype-tfidfl20_01_-uid'

expt_runs['rcv2_p_fixed']= OrderedDict() 
expt_runs['rcv2_p_fixed']['3-400-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 400 -ql 3 -reload '+chkpt['3-400-p_fixed']+'-EP200-params.npz -params '+chkpt['3-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed']['2-400-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 400 -ql 2 -reload '+chkpt['2-400-p_fixed']+'-EP200-params.npz -params '+chkpt['2-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed']['1-400-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 400 -ql 1 -reload '+chkpt['1-400-p_fixed']+'-EP200-params.npz -params '+chkpt['1-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed']['3-100-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 100 -ql 3 -reload '+chkpt['3-100-p_fixed']+'-EP200-params.npz -params '+chkpt['3-100-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed']['2-100-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 100 -ql 2 -reload '+chkpt['2-100-p_fixed']+'-EP200-params.npz -params '+chkpt['2-100-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed']['1-100-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only -pl 2 -ns 100 -ep 100 -qh 100 -ql 1 -reload '+chkpt['1-100-p_fixed']+'-EP200-params.npz -params '+chkpt['1-100-p_fixed']+'-config.pkl'

expt_runs['rcv2_p_fixed_random']= OrderedDict() 
expt_runs['rcv2_p_fixed_random']['3-400-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 400 -ql 3 -reload '+chkpt['3-400-p_fixed']+'-EP200-params.npz -params '+chkpt['3-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed_random']['2-400-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 400 -ql 2 -reload '+chkpt['2-400-p_fixed']+'-EP200-params.npz -params '+chkpt['2-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed_random']['1-400-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 400 -ql 1 -reload '+chkpt['1-400-p_fixed']+'-EP200-params.npz -params '+chkpt['1-400-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed_random']['3-100-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 100 -ql 3 -reload '+chkpt['3-100-p_fixed']+'-EP200-params.npz -params '+chkpt['3-100-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed_random']['2-100-p_fixed']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 100 -ql 2 -reload '+chkpt['2-100-p_fixed']+'-EP200-params.npz -params '+chkpt['2-100-p_fixed']+'-config.pkl'
expt_runs['rcv2_p_fixed_random']['1-100-p_fixed']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype q_only_random -pl 2 -ns 100 -ep 100 -qh 100 -ql 1 -reload '+chkpt['1-100-p_fixed']+'-EP200-params.npz -params '+chkpt['1-100-p_fixed']+'-config.pkl'

expt_runs['rcv2_q_vary']= OrderedDict() 
expt_runs['rcv2_q_vary']['3-400-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 400 -ql 3'
expt_runs['rcv2_q_vary']['3-400-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 400 -ql 3'
expt_runs['rcv2_q_vary']['2-400-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 400 -ql 2'
expt_runs['rcv2_q_vary']['2-400-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 400 -ql 2'
expt_runs['rcv2_q_vary']['1-400-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 400 -ql 1'
expt_runs['rcv2_q_vary']['1-400-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 400 -ql 1'
expt_runs['rcv2_q_vary']['3-100-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 100 -ql 3'
expt_runs['rcv2_q_vary']['3-100-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 100 -ql 3'
expt_runs['rcv2_q_vary']['2-100-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 100 -ql 2'
expt_runs['rcv2_q_vary']['2-100-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 100 -ql 2'
expt_runs['rcv2_q_vary']['1-100-none']   = gpu_0_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 200 -qh 100 -ql 1'
expt_runs['rcv2_q_vary']['1-100-finopt']   = gpu_1_full+' '+'python2.7 train.py -dset rcv2 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 200 -qh 100 -ql 1'

"""
Experiments on the WikiCorpus Dataset
"""
expt_runs['wikicorp'] = OrderedDict() 
expt_runs['wikicorp']['2-none']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 200 -ep 50'
expt_runs['wikicorp']['2-finopt'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 200 -ep 50'
expt_runs['wikicorp']['0-none']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 200 -ep 500'
expt_runs['wikicorp']['0-finopt'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype finopt -pl 0 -ns 200 -ep 500'
expt_runs['wikicorp']['2-ar10k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 200 -ep 500 -ar 10000'
expt_runs['wikicorp']['0-ar10k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 200 -ep 500 -ar 10000'
expt_runs['wikicorp']['2-ar50k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 200 -ep 500 -ar 50000'
expt_runs['wikicorp']['0-ar50k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 200 -ep 500 -ar 50000'
expt_runs['wikicorp']['2-ar100k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 200 -ep 500 -ar 100000'
expt_runs['wikicorp']['0-ar100k']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp -ds 100 -itype tfidf -nl relu -otype none -pl 0 -ns 200 -ep 500 -ar 100000'

expt_runs['wikicorp_sparsity'] = OrderedDict() 
expt_runs['wikicorp_sparsity']['1000-2-finopt'] = gpu_0_full+' '+'python2.7 train.py -dset wikicorp_1000 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 50'
expt_runs['wikicorp_sparsity']['5000-2-finopt'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp_5000 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 50'
expt_runs['wikicorp_sparsity']['10000-2-finopt'] = gpu_0_full+' '+'python2.7 train.py -dset wikicorp_10000 -ds 100 -itype tfidf -nl relu -otype finopt -pl 2 -ns 100 -ep 50'
expt_runs['wikicorp_sparsity']['1000-2-none'] = gpu_0_full+' '+'python2.7 train.py -dset wikicorp_1000 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 50'
expt_runs['wikicorp_sparsity']['5000-2-none'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp_5000 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 50'
expt_runs['wikicorp_sparsity']['10000-2-none'] = gpu_0_full+' '+'python2.7 train.py -dset wikicorp_10000 -ds 100 -itype tfidf -nl relu -otype none -pl 2 -ns 100 -ep 50'

"""
* Evaluating different models: comprise evaluating and saving Ejacob and/or CJacob
* Open and setup all the evaluation scripts to point to the relevant checkpoints
"""
expt_runs['wikicorp-large'] = OrderedDict() 
expt_runs['wikicorp-large']['2-none']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp-large -ds 300 -itype tfidf -nl relu -otype none -pl 2 -ns 200 -ep 50 -uid final'
expt_runs['wikicorp-large']['2-finopt'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp-large -ds 300 -itype tfidf -nl relu -otype finopt -pl 2 -ns 200 -ep 50 -uid final'
expt_runs['wikicorp-large']['0-none']   = gpu_0_full+' '+'python2.7 train.py -dset wikicorp-large -ds 300 -itype tfidf -nl relu -otype none -pl 0 -ns 200 -ep 50 -uid final'
expt_runs['wikicorp-large']['0-finopt'] = gpu_1_full+' '+'python2.7 train.py -dset wikicorp-large -ds 300 -itype tfidf -nl relu -otype finopt -pl 0 -ns 200 -ep 50 -uid final'

""" Evaluate Wikicorp """
expt_runs['wikicorp_evaluate'] = OrderedDict() 
expt_runs['wikicorp_evaluate']['2-none']   = gpu_0_full+' '+'python2.7 evaluateWikipedia.py pl-2-none'
expt_runs['wikicorp_evaluate']['2-finopt'] = gpu_1_full+' '+'python2.7 evaluateWikipedia.py pl-2-finopt'
expt_runs['wikicorp_evaluate']['0-none']   = gpu_0_full+' '+'python2.7 evaluateWikipedia.py pl-0-none'
expt_runs['wikicorp_evaluate']['0-finopt'] = gpu_1_full+' '+'python2.7 evaluateWikipedia.py pl-0-finopt'

""" Evaluate Wikicorp (Conditional Jacobian) """
expt_runs['wikicorp_conditional_evaluate'] = OrderedDict() 
expt_runs['wikicorp_conditional_evaluate']['2-none']   = gpu_0_full+' '+'python2.7 evaluateConditionalWikipedia.py pl-2-none'
expt_runs['wikicorp_conditional_evaluate']['2-finopt'] = gpu_1_full+' '+'python2.7 evaluateConditionalWikipedia.py pl-2-finopt'
expt_runs['wikicorp_conditional_evaluate']['0-none']   = gpu_0_full+' '+'python2.7 evaluateConditionalWikipedia.py pl-0-none'
expt_runs['wikicorp_conditional_evaluate']['0-finopt'] = gpu_1_full+' '+'python2.7 evaluateConditionalWikipedia.py pl-0-finopt'

for expt in expt_runs[expt_type]:
    print 'screen -S '+expt
    print expt_runs[expt_type][expt]
