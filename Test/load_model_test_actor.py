import torch as T
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torch.distributions.normal import Normal
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from networks import ActorNetwork, CriticNetwork
import seaborn as sb
import h5py
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

from Grid import Freq_Dynamics



if True:
    font = FontProperties()
    font.set_family('serif')
    font.set_name('Times New Roman')
    font.set_size(12)
    font_size = 12
    rcParams['font.size'] = font_size
    plt.rcParams['lines.linewidth'] = 2
    print("test")
    Data = []
    filename = 'mpc_L0pt44.mat'
      
    datavar = 'datavar'
    f = h5py.File(filename, 'r')
    Data.append(f[datavar][()])

    stop_time = 100.02
    env = Freq_Dynamics(
    Q11=0.2,
    Q22=0.3,
    R11=0.005,
    reset_time=0.0,
    stop_time=100,
    load_range=[-0.2, 0.2],
    compile=False,
    train=False
    )
    model = T.load("norm_Actormodel_11_8_epi3550")

    plstate = []
    input_power = []
    action_timer4 = []
    temp = []

    counter = 0

    timer = 0.0 
    prev_state = env.reset()

    done = False
    sum_reward = 0
    freqstate1 = []
    while not done:
        prev_state = T.Tensor([prev_state]) 
        action, _ = model(prev_state)
        action = T.tanh(action) * 0.5
        action = action.cpu().detach().numpy()[0]

        observation_, reward, _, _, _, done, info =  env.step(np.array([0.0]))
        prev_state = observation_
        counter += 1
        input_power.append(action)
        plstate.append(observation_)
        freqstate1.append(observation_[0])
        if done:
            break


    plstate2 = []
    input_power2 = []
    counter = 0
    prev_state = env.reset()

    ROCOF = 0
    done = False
    freqstate = []
    count = 0
    Act = 0
    Reward_box = []
    R1_box = []
    R2_box = []
    R3_box = []
    old_freq = abs(prev_state[0])
    while not done:
        ROCOF = prev_state[1]
        prev_state = T.Tensor([prev_state]) 
        action, _ = model(prev_state)
        action = T.tanh(action) * 0.5
        action = action.cpu().detach().numpy()[0] 
        observation_, reward, r1, r2, r3, done, info =  env.step(np.array([action]))
        prev_state = observation_
        counter += 0.02
        input_power2.append(action)
        plstate2.append(observation_)
        Reward_box.append(reward)
        R1_box.append(r1)
        R2_box.append(r2)
        R3_box.append(r3)
        sum_reward += reward
        freqstate.append(observation_[0])
        if abs(prev_state[0])> old_freq:
            old_freq= abs(prev_state[0])
            count += 0.02

        if done:
            break

    space = 0.2
    time = np.arange(0,stop_time,0.02)
    print('Nadir no FFR: ', max(abs(np.array(freqstate1))))
    print('Nadir RL: ', max(abs(np.array(freqstate))))
    print('Nadir MPC: ', max(abs(Data[0][:,3])))
    print('Peak Power RL: ', max(abs(np.array(input_power2))))
    print('Peak Power MPC : ', max(abs(Data[0][:,5])))

    print("improvement RL: ", (max(abs(np.array(freqstate1)))- max(abs(np.array(freqstate))))*100/ max(abs(np.array(freqstate1))))
    print("improvement MPC: ", (max(abs(np.array(freqstate1)))- max(abs(Data[0][:,3])))*100/ max(abs(np.array(freqstate1))))
    
    fig, ax = plt.subplots(1, 3, figsize=(14, 4), constrained_layout=True)
    ax[0].plot(
        np.arange(0,stop_time,0.02),
        [plstate[k][0] for k in range(len(plstate))],
        label="no FFR"
    )

    ax[0].plot(
        np.arange(0,stop_time,0.02),
        [plstate2[k][0] for k in range(len(plstate2))],
        label="SAC RL-based Control",
        color = 'C1'
    )

    ax[0].plot(
        np.arange(0,stop_time,0.02),
        Data[0][:,3],
        label="MPC",
        color = 'C2'
    )


    ax[0].plot(np.arange(0.0, stop_time, 0.02), np.full(len(np.arange(0.0, stop_time, 
                                                           0.02)), -0.0117), label='UFLS T1: 59.3 Hz', color = 'olive', linewidth = 1.6, linestyle="--")
    ax[0].plot(np.arange(0.0, stop_time, 0.02), np.full(len(np.arange(0.0, stop_time, 
                                                            0.02)), -0.0183), label='UFLS T2: 58.9 Hz', color = 'blueviolet', linewidth = 1.6, linestyle="--")
    ax[0].plot(np.arange(0.0, stop_time, 0.02), np.full(len(np.arange(0.0, stop_time, 
                                                            0.02)), -0.025), label='UFLS T3: 58.5 Hz', color = 'hotpink', linewidth = 1.6, linestyle="--")


    ax[0].set_xlabel("time [s]", fontproperties=font, fontsize=font_size)
    ax[0].set_ylabel("$\Delta\omega$ [pu]", fontproperties=font, fontsize=font_size)
    ax[0].legend(loc=0, prop=font, fontsize=12, labelspacing=space)
    ax[0].grid(True, linestyle="-.")

    ax[1].plot(
        np.arange(0,stop_time,0.02),
        [plstate[k][1] for k in range(len(plstate))],
        label="no FFR"
    )

    ax[1].plot(
        np.arange(0,stop_time,0.02),
        [plstate2[k][1] for k in range(len(plstate2))],
        label="SAC RL-based Control",
        color = 'C1'
    )

    ax[1].plot(
        np.arange(0,stop_time,0.02),
        Data[0][:,4],
        label="MPC",
        color = 'C2'
    )
    ax[1].set_xlabel("time [s]", fontproperties=font, fontsize=font_size)
    ax[1].set_ylabel("$\dot{\Delta\omega}$ [pu]", fontproperties=font, fontsize=font_size)
    ax[1].legend(loc=0, prop=font, fontsize=12, labelspacing=space)
    ax[1].grid(True, linestyle="-.")


    y = np.array(input_power2).flatten()
    positive_indices = np.where(y > 0)[0]
    x_positive = time[positive_indices]
    y_positive = y[positive_indices]

    ax[2].plot(
        np.arange(0,stop_time,0.02),
        input_power2,
        label="SAC RL-based Control", color = 'C1'
    )

    ax[2].plot(
        np.arange(0,stop_time,0.02),
        Data[0][:,5],
        label="MPC", color = 'C2'
    )


    ax[2].set_xlabel("time [s]", fontproperties=font, fontsize=font_size)
    ax[2].set_ylabel("$\Delta P_{inv}$ [pu]", fontproperties=font, fontsize=font_size)
    ax[2].legend(loc=0, prop=font, fontsize=12, labelspacing=space)
    ax[2].grid(True, linestyle="-.")

    plt.savefig("result.png", dpi=600)
    plt.show()
