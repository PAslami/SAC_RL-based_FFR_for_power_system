import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sb
import numpy as np
import h5py
import torch as T
import numpy as np
from networks import ActorNetwork, CriticNetwork
from Grid import Freq_Dynamics
import tensorflow as tf
from tensorflow.keras import layers
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams


font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(12)
font_size = 12
rcParams['font.size'] = font_size
plt.rcParams['lines.linewidth'] = 2

Data = []
t0 = 0
t1 = np.inf
filename = ['MPC_data\mpc_11_2_L-0pt6.mat', 'MPC_data\mpc_11_2_L-0pt58.mat', 'MPC_data\mpc_11_2_L-0pt56.mat','MPC_data\mpc_11_2_L-0pt54.mat', 'MPC_data\mpc_11_2_L-0pt52.mat',
    'MPC_data\mpc_11_2_L-0pt5.mat', 'MPC_data\mpc_11_2_L-0pt48.mat', 'MPC_data\mpc_11_2_L-0pt46.mat','MPC_data\mpc_11_2_L-0pt44.mat', 'MPC_data\mpc_11_2_L-0pt42.mat',
    'MPC_data\mpc_11_2_L-0pt4.mat', 'MPC_data\mpc_11_2_L-0pt38.mat', 'MPC_data\mpc_11_2_L-0pt36.mat','MPC_data\mpc_11_2_L-0pt34.mat', 'MPC_data\mpc_11_2_L-0pt32.mat',
    'MPC_data\mpc_11_2_L-0pt3.mat', 'MPC_data\mpc_11_2_L-0pt28.mat', 'MPC_data\mpc_11_2_L-0pt26.mat','MPC_data\mpc_11_2_L-0pt24.mat', 'MPC_data\mpc_11_2_L-0pt22.mat',        
    'MPC_data\mpc_10_25_L-0pt2.mat', 'MPC_data\mpc_10_25_L-0pt18.mat','MPC_data\mpc_10_25_L-0pt16.mat','MPC_data\mpc_10_25_L-0pt14.mat', 'MPC_data\mpc_10_25_L-0pt12.mat',
    'MPC_data\mpc_10_25_L-0pt1.mat','MPC_data\mpc_10_25_L-0pt08.mat', 'MPC_data\mpc_10_25_L-0pt06.mat', 'MPC_data\mpc_10_25_L-0pt04.mat', 'MPC_data\mpc_10_25_L-0pt02.mat', 
    'MPC_data\mpc_10_25_L0pt0.mat','MPC_data\mpc_10_25_L0pt02.mat', 'MPC_data\mpc_10_25_L0pt04.mat', 'MPC_data\mpc_10_25_L0pt06.mat', 'MPC_data\mpc_10_25_L0pt08.mat', 
    'MPC_data\mpc_10_25_L0pt1.mat', 'MPC_data\mpc_10_25_L0pt12.mat', 'MPC_data\mpc_10_25_L0pt14.mat', 'MPC_data\mpc_10_25_L0pt16.mat', 'MPC_data\mpc_10_25_L0pt18.mat', 
    'MPC_data\mpc_10_25_L0pt2.mat', 'MPC_data\mpc_11_2_L0pt22.mat', 'MPC_data\mpc_11_2_L0pt24.mat', 'MPC_data\mpc_11_2_L0pt26.mat', 'MPC_data\mpc_11_2_L0pt28.mat',
    'MPC_data\mpc_10_27_L0pt3.mat', 'MPC_data\mpc_11_2_L0pt32.mat', 'MPC_data\mpc_11_2_L0pt34.mat', 'MPC_data\mpc_11_2_L0pt36.mat', 'MPC_data\mpc_11_2_L0pt38.mat',
    'MPC_data\mpc_11_2_L0pt4.mat', 'MPC_data\mpc_11_2_L0pt42.mat', 'MPC_data\mpc_11_2_L0pt44.mat', 'MPC_data\mpc_11_2_L0pt46.mat', 'MPC_data\mpc_11_2_L0pt48.mat',
    'MPC_data\mpc_10_27_L0pt5.mat', 'MPC_data\mpc_11_2_L0pt52.mat', 'MPC_data\mpc_11_2_L0pt54.mat', 'MPC_data\mpc_11_2_L0pt56.mat', 'MPC_data\mpc_11_2_L0pt58.mat',
    'MPC_data\mpc_11_2_L0pt6.mat']

n = 0
for name in filename:
    datavar = 'datavar'
    f = h5py.File(name, 'r')
    Data.append(f[datavar][()])
    f.close()

    tk = (Data[n][:,0] >= t0) & (Data[n][:,0]<=t1)
    Data[n] = Data[n][tk, :]
    n += 1

nadirMPC = []
nadir_nocontrol = []

ROCOFMPC = []

for i in range(61):
    if i >= 20 and i<=40: 
        nadirMPC.append(max(abs(Data[i][:,1])))
        nadir_nocontrol.append(max(abs(Data[i][:,3])))
        ROCOFMPC.append(max(abs(Data[i][:,2])))
    else:
        nadirMPC.append(max(abs(Data[i][:,3])))
        nadir_nocontrol.append(max(abs(Data[i][:,1])))
        ROCOFMPC.append(max(abs(Data[i][:,4])))


env = Freq_Dynamics(
    Q11=0.2,
    Q22=0.3,
    R11=0.005,
    reset_time=0.0,
    stop_time=100,
    load_range=[-0.2, 0.2],
    load_change_time=20,
    compile=False,
    train=False
    )

model = T.load('norm_Actormodel_11_8_epi3550')


load = np.round(np.arange(-0.6, 0.62, 0.02), 2)
nadirRL = []
ROCOFRL =[]
INPUT = []

for L in load:
    freqstate = []
    rocof = []
    input = []
    done = False
    prev_state = env.reset(L)
    while not done:
        prev_state = T.Tensor([prev_state]) 
        action, _ = model(prev_state)
        action = T.tanh(action) * 0.5
        action = action.cpu().detach().numpy()[0] 

        observation_, reward, done, info =  env.step(np.array([action]))
        prev_state = observation_
        freqstate.append(observation_[0])
        rocof.append(observation_[1])
        input.append(action)
    
    nadirRL.append(max(abs(np.array(freqstate))))
    ROCOFRL.append(max(abs(np.array(rocof))))
    INPUT.append(max(abs(np.array(input))))

load = np.round(np.arange(-0.6, 0.62, 0.02), 2)
ROCOF_nocontrol2 = []


for L in load:
    freqstate = []
    rocof = []
    input = []
    done = False
    prev_state = env.reset(L)
    while not done:
        prev_state = T.Tensor([prev_state]) 
        action, _ = model(prev_state)
        action = T.tanh(action) * 0.5
        action = action.cpu().detach().numpy()[0]

        observation_, reward, done, info =  env.step(np.array([0.0]))
        prev_state = observation_
        rocof.append(observation_[1])
    ROCOF_nocontrol2.append(max(abs(np.array(rocof))))




# baseline = np.full(61, 0.01)
#### plot with actual values 

neg_nadir_nocontrol = [-x for x in nadir_nocontrol]
neg_nadirRL = [-x for x in nadirRL]
neg_nadirMPC = [-x for x in nadirMPC]

neg_ROCOF_nocontrol2 = [-x for x in ROCOF_nocontrol2]
neg_ROCOFRL = [-x for x in ROCOFRL]
neg_ROCOFMPC = [-x for x in ROCOFMPC]

middle_position = len(neg_nadir_nocontrol) // 2

neg_nadir_nocontrol = neg_nadir_nocontrol[middle_position:]
neg_nadirRL = neg_nadirRL[middle_position:]
neg_nadirMPC = neg_nadirMPC[middle_position:]

neg_ROCOF_nocontrol2 = neg_ROCOF_nocontrol2[middle_position:]
neg_ROCOFRL = neg_ROCOFRL[middle_position:]
neg_ROCOFMPC = neg_ROCOFMPC[middle_position:]

# plt.figure(figsize=(8,8))
plt.figure(figsize=(6,6), constrained_layout=True)
plt.plot(np.arange(0.0, 0.62, 0.02), np.array(neg_nadir_nocontrol), '-o', markersize=4, label='nadir- no FFR', color = 'C0')
plt.plot(np.arange(0.0, 0.62, 0.02), np.array(neg_nadirRL), '--bo', markersize=4, label='nadir- SAC RL-based FFR ', color = 'C1')
plt.plot(np.arange(0.0, 0.62, 0.02), np.array(neg_nadirMPC), '--bo', markersize=4, label='nadir- MPC', color = 'C2')

# plt.plot(np.arange(-0.6, 0.62, 0.02), np.array(nadirRL2), '--bo', label='nadir- SAC-RL2', color = 'pink')
plt.plot(np.arange(0.0, 0.62, 0.02), np.full(len(np.arange(0.0, 0.62, 
                                                           0.02)), -0.0117), label='UFLS T1: 59.3 Hz ', color = 'olive', linewidth = 1.6, linestyle="--")
plt.plot(np.arange(0.0, 0.62, 0.02), np.full(len(np.arange(0.0, 0.62, 
                                                           0.02)), -0.0183), label='UFLS T1: 58.9 Hz ', color = 'blueviolet', linewidth = 1.6, linestyle="--")
plt.plot(np.arange(0.0, 0.62, 0.02), np.full(len(np.arange(0.0, 0.62, 
                                                           0.02)), -0.025), label='UFLS T1: 58.5 Hz ', color = 'hotpink', linewidth = 1.6, linestyle="--")

plt.axvline(x=0.0, color='black', linestyle='--', linewidth = 0.5)
plt.xlabel('load change $\Delta P_{inv}$ [pu]', fontproperties=font)
plt.ylabel('Nadir of $\Delta \omega$ [pu]', fontproperties=font)
# plt.title('Frequency nadir with load change', fontsize = 12)
# plt.set_xlabel('x-axis', fontsize = 12)
plt.grid(True, linestyle="-.")
plt.legend(loc=0, prop=font, fontsize=12)
plt.savefig("models_eval.png", dpi=600)
plt.show()
