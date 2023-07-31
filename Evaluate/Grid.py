import numpy as np
import gym
from gym.spaces import Box
import sys
import os
from typing import List

sys.path.insert(1, os.path.join(os.path.split(__file__)[0], "simulation_code"))
from freq_model_pyinterface import freq_model

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class Freq_Dynamics(gym.Env):
    def __init__(self, Q11: float, Q22: float, R11: float, reset_time: float, stop_time: float, load_range: List[str], load_change_time: float, compile: bool, train: bool) -> None:
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
        load_range : List[float]
            Range of load change for training
        load_change_time: float
            Time at which load change is required
        compile : bool
            Whether to compile. Must compile for first time.
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
            self.load_change_time,
            self.compile,
            self.train
        ) = (
            Q11,
            Q22,
            R11,
            reset_time, 
            stop_time,
            load_range,
            np.array([load_change_time], dtype=np.float64),
            compile,
            train
        )

        self.model = freq_model(
            compile=self.compile
        )

    def reset(self, load):
        u = np.array([0.0])
        if self.train:
            self.L = np.random.uniform(self.load_range[0], self.load_range[1], size=(1,))
        else:
            self.L = np.array([load], dtype=np.float64)

        self.model.reset(u, self.L, self.load_change_time)

        return self.model.x_est.copy()
    
    def step(self, action):
        u = action.astype(np.float64)
        cost = self.Q11*(self.model.x_est[0])**2 + self.Q22*(self.model.x_est[1])**2 + self.R11*(action[0])**2
        self.model.one_step(u, self.L, self.load_change_time)

        done = True if self.model.current_time > self.stop_time else False
        return self.model.x_est.copy(), -cost, done, {}


if __name__=="__main__":
    import matplotlib.pyplot as plt
    g = Freq_Dynamics(
        Q11=0.2,
        Q22=0.3,
        R11=0.005,
        reset_time=0.0,
        stop_time=10,
        load_range=[-0.2, 0.2],
        load_change_time=5,
        compile=True,
        train=False
    )

    done = False
    x = []

    obs = g.reset()
    while not done:
        action = np.array([0.0], dtype=np.float64)

        x.append(obs[0])
        obs, reward, done, info = g.step(action)

    plt.plot(x)
    plt.show()

