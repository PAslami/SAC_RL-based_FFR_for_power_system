"""
Filename:       sac_ffr_train.py
Written by:     Pooja Aslami
"""

import numpy as np
import torch as T
from sacFFR.Train.sac_modules.sac_torch import Agent
from sacFFR.Train.sac_modules.utils import plot_learning_curve, norm_reward
import os
from sacFFR.Train.sac_modules.sac_parser import create_parser
from sacFFR.Environments.Grid import Freq_Dynamics 

def get_inpt_args():
    parser = create_parser()
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print(f"[RLFDI WARNING]: {unknown} unknown argument(s)")

    return args

def setup_env_agent(args):
    print(f"Training with following parameters: {args}")
    env = Freq_Dynamics(
    Q11=args.Q1,
    Q22=args.Q2,
    R11=args.R1,
    reset_time=args.reset_time,
    stop_time=args.stop_time,
    load_range=[-args.load_range, args.load_range],
    compile=True,
    train=args.train,
    test_load= args.test_load
    )
    for dir_path in [args.models_dir, args.chkpt_dir]:
        os.makedirs(dir_path, exist_ok=True)

    agent = Agent(input_dims=(args.input_size,), env= env, n_actions=args.action_size)
    if args.load_checkpoint:
        agent.load_models()
    return env, agent

def train(args, env, agent):
    mu, var, n = 0.0, 0.0, 0
    best_score = float('-inf')
    score_history = []
    for i in range(args.n_episodes):
        observation = env.reset()
        done = False
        score = 0
        while not done:
            action, _ = agent.choose_action(observation)
            observation_, reward, done, load = env.step(np.array([action]))
            norm_rew, mu, var, n = norm_reward(reward, mu, var, n)
            score += reward  
            agent.remember(observation, action, norm_rew, observation_, done)   
            agent.learn()
            observation = observation_
        score_history.append(score)
        avg_score = np.mean(score_history[-10:])
        if avg_score > best_score:
            best_score = avg_score
            if args.save_checkpoint:
                agent.save_models()
        print('episode ', i, 'score %.5f' % score, 'avg_score %.5f' % avg_score, 'load', load[0], flush = True)
        if i%50==0:  ### for saving policy in regular interval
            T.save(agent.actor, f"{args.models_dir}/Actormodel_epi_{i}") 
    plot_learning_curve([i+1 for i in range(args.n_episodes)], score_history, args.fig_file)


if __name__ == "__main__":
    args = get_inpt_args()
    args.train = True
    # args.load_checkpoint = True
    env, agent = setup_env_agent(args)
    train(args, env, agent)