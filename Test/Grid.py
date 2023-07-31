"""
Filename:       Grid.py
Date:           10/16/2022
Written by:     Niranjan Bhujel
"""

import numpy as np
import gym
from gym.spaces import Box
import sys
import os
from typing import List
import math 

sys.path.insert(1, os.path.join(os.path.split(__file__)[0], "simulation_code"))
from freq_model_pyinterface import freq_model

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class Freq_Dynamics(gym.Env):
    def __init__(self, Q11: float, Q22: float, R11: float, reset_time: float, stop_time: float, load_range: List[str], compile: bool, train: bool) -> None:
        """
        Simplified frequency dynamics model.

        Parameters
        ----------
        Q11 : float
            Value of Q11 for reward calculation
        Q22 : float
            Value of Q22 for reward calculation
        R11 : float
            Value of R11 for reward calculation
        reset_time : float
            Time to start collecting data for training
        stop_time : float
            Time upto which simulation is to be run
        load_range : List[str]
            Range of load change for training
        compile : bool
            Whether to compile. Must compile for first time. After that, it can be set to `False`.
        train : bool
            If set to `True`, random load change is done. If `False`, load change of 0.2 p.u. is done.
        """
        super().__init__()

        self.action_space = Box(
            low=np.array([-0.5]),
            high=np.array([0.5])
        )

        self.observation_space = Box(
            low=np.array([-0.1, -0.1, -0.1]),
            high=np.array([0.1, 0.1, 0.1])
        )
        (
            self.Q11,
            self.Q22,
            self.R11,
            self.reset_time,
            self.stop_time,
            self.load_range,
            self.compile,
            self.train
        ) = (
            Q11,
            Q22,
            R11,
            reset_time, 
            stop_time,
            load_range,
            compile,
            train
        )

        self.model = freq_model(
            compile=self.compile
        )
        
        self.t_step = 1.0

    def reset(self):
        u = np.array([0.0])
        if self.train:
            self.L = np.random.uniform(self.load_range[0], self.load_range[1], size=(1,))
        else:
            self.L = np.array([0.44], dtype=np.float64)

        self.model.reset(u, np.array([0.0]))

        return self.model.x_est.copy()
    
    def step(self, action):
        u = action.astype(np.float64)
        cost_1 = self.Q11*(self.model.x_est[0])**2
        cost_2 = self.Q22*(self.model.x_est[1])**2
        cost_3 = self.R11*(action[0])**2
        cost = cost_1 + cost_2 + cost_3
        
        L = self.L if self.model.current_time >= self.t_step else 0.0
        L = np.array([L])
        # cost = self.Q11*(math.exp(abs(self.model.x_est[0]))-1) + self.Q22*(math.exp(abs(self.model.x_est[1]))-1)+ self.R11*(action[0])**2 ### exponential cost
        # cost = (np.power(1.5,abs(self.model.x_est[0])*1500)) + (np.power(1.5, abs(self.model.x_est[1])*1500))+ self.R11*(action[0])**2
        self.model.one_step(u, L)

        done = True if self.model.current_time > self.stop_time else False
        return self.model.x_est.copy(), -cost, -cost_1, -cost_2, -cost_3, done, self.L
