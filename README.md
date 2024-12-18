# Fast Frequency Response (FFR) to Power System Frequency Dynamics Using Soft Actor-Critic Algorithm
This repository contains the source code required to reproduce the results presented in the following paper:  
[A Soft Actor-Critic Approach for Power System Fast Frequency Response](https://ieeexplore.ieee.org/document/10318617?denied=)  
## Installation
```
conda create --name sacffr python=3.10
conda activate sacffr
pip install -e .
```

## Training 
The training file to train the SAC agent to provide FFR to the frequency dynmaics of the power grid is located in 'sacFFR/Train'. To trian the agent for 2000 episodes, run the following code. 
``` python 
python sacFFR/Train/sac_ffr_train.py --n-episodes 2000 
``` 
The configurable arguments are available in 'sacFFR/Train/sac_modules/sac_parser.py'

## Evaluation 
The plotting files to test the trained SAC agent (sacFFR/Data/trained_sac/norm_Actormodel_11_8_epi3550) to provide FFR to the frequency dynmaics of the power grid is located in 'sacFFR/Evaluate'. To generate the testing plots from the paper, run the following code. 
``` python 
python sacFFR/Evaluate/policy_eval.py --fig-file "policy_eval.png"
python sacFFR/Evaluate/multi_step_load_eval.py --fig-file "multi_step_load_eval.png"
python sacFFR/Evaluate/compute_time.py --fig-file "compute_time.png"
```

