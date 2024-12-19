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

## Citation
If you find this code useful, kindly consider citing it as follows:
```
@INPROCEEDINGS{10318617,
  author={Aslami, Pooja and Aryal, Tara and Bhujel, Niranjan and Rai, Astha and Rekabdarkolaee, Hossein Moradi and Hansen, Timothy M.},
  booktitle={2023 North American Power Symposium (NAPS)}, 
  title={A Soft Actor-Critic Approach for Power System Fast Frequency Response}, 
  year={2023},
  volume={},
  number={},
  pages={1-6},
  keywords={Time-frequency analysis;Software packages;Computational modeling;Power system dynamics;Power system stability;Mathematical models;Stability analysis;Fast Frequency Response;Power System Frequency Dynamics;Reinforcement Learning;Soft Actor-Critic},
  doi={10.1109/NAPS58826.2023.10318617}}
```
Feel free to reach out via email at Pooja.Aslami@jacks.sdstate.edu for any inquiries.
