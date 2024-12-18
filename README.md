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
The training file to train the SAC agent to provide FFR to the frequency dynmaics of the power grid is located in 'sacFFR/Train'.
``` python 
python sacFFR/Train/sacffr_train.py 
``` 
