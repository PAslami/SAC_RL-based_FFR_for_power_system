# MAINLOOP with normalization

import numpy as np
import torch as T
import matplotlib.pyplot as plt
from sac_torch import Agent
from utils import plot_learning_curve
import os

from Grid import Freq_Dynamics

def new_mu(mu_init, n, new_obs):
    return((n * mu_init + new_obs) / (n + 1))

def new_var(mu_init, var_init, mu_new, n, new_obs):
    return(((n * var_init) / (n + 1))+(((new_obs - mu_new)**2) /n ))

if __name__ == '__main__':
    env = Freq_Dynamics(
        Q11=0.2,
        Q22=0.3,
        R11=0.005,
        reset_time=0.0,
        stop_time=100,
        load_range=[-0.2, 0.2],
        compile=True,
        train=True
    )
    models_dir = "norm_SAC/100sec"
    chkpt_dir = 'tmp/sac'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    if not os.path.exists(chkpt_dir):
        os.makedirs(chkpt_dir)
    agent = Agent(input_dims=(3,), env= env, n_actions=1)

    n_games = 4001

    filename = 'average_reward_norm_SAC.png'
    name = "norm_Actormodel_epi_"

    figure_file = 'plots/' + filename

    best_score = float('-inf')
    score_history = []
    load_history = []
    load_checkpoint = False

    n = 0
    mu_init = 0
    new_vari = 0
    for i in range(n_games):
        observation = env.reset()
        done = False
        score = 0
        while not done:
            action, _ = agent.choose_action(observation)
            observation_, reward, done, load = env.step(np.array([action]))
            #####Reward normalization####
            if n ==0:
                new_mean = reward
                norm_reward = reward
            elif n ==1:
                new_mean = np.mean([mu_init, reward])
                new_vari = np.var([mu_init, reward])
                norm_reward = (reward-new_mean)/np.sqrt(new_vari*((n + 1) / n)) ###unbiased sigma
            else:
                new_mean = new_mu(mu_init, n, reward)
                new_vari = new_var(mu_init, var_init, new_mean, n, reward)
                norm_reward = (reward-new_mean)/np.sqrt(new_vari*((n + 1) / n))
            mu_init = new_mean
            var_init = new_vari
            n += 1
            score += reward  
            agent.remember(observation, action, norm_reward, observation_, done)   
            if not load_checkpoint:
                agent.learn()
            observation = observation_
        score_history.append(score)
        avg_score = np.mean(score_history[-10:])
        if avg_score > best_score:
            best_score = avg_score
            if not load_checkpoint:
                agent.save_models()

        print('episode ', i, 'score %.5f' % score, 'avg_score %.5f' % avg_score, 'load', load[0], flush = True)

        if i%50==0:
            T.save(agent.actor, f"{models_dir}/{name+str(i)}") 

    if not load_checkpoint:
        x = [i+1 for i in range(n_games)]
        plot_learning_curve(x, score_history, figure_file)
        plt.grid()
        plt.ylabel("score")
        plt.xlabel("episodes")
