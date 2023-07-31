"""
Filename:       freq_model_pyinterface.py
Written by:     Niranjan Bhujel
Date:           2022-10-16
"""

import os
import ctypes
import numpy as np
import h5py
import time
import argparse


class freq_model:
    def __init__(self, out_lib_name: str="freq_model_lib.so", step_time: float=0.02, compile: bool=True):
        """
        Class to simulate the freq_model system. The model input and output are shown below:
        
        Input:
            u [1]
            L [1]
            
        Output:
            x_est [3]
            x [2]
            
        """
        filepath = __file__
        filepath = os.path.split(filepath)[0]
        if filepath=="":
            filepath = "./"

        if compile:
            compile_cmd = "gcc -fPIC -shared -O3 -lm " + '"' +\
                os.path.join(filepath, 'freq_model_interface.c') + '"' + ' "' +\
                os.path.join(filepath, 'sim_code"/*.c') + ' -o ' + '"' +\
                os.path.join(filepath, out_lib_name) + '"'
            # print(compile_cmd)
            os.system(compile_cmd)

        self.start_time = 0.0
        self.step_time = step_time
        self.current_time = self.start_time
        self.next_time = self.current_time + self.step_time
        
        self.freq_model_system = ctypes.cdll.LoadLibrary(os.path.join(filepath, out_lib_name))

        self.freq_model_system.initialize.restype = None
        self.freq_model_system.initialize.argtypes = [
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            
        ]

        self.freq_model_system.one_step.restype = None
        self.freq_model_system.one_step.argtypes = [
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            np.ctypeslib.ndpointer(dtype=np.float64),
            
        ]

        self.x_est = np.zeros((3,), dtype=np.float64)
        self.x = np.zeros((2,), dtype=np.float64)
        
    
    def reset(self, u: np.ndarray, L: np.ndarray):
        """
        Reset the simulation back to initial state.
        """
        self.current_time = self.start_time
        self.next_time = self.current_time + self.step_time
        self.freq_model_system.initialize(u, L,  self.x_est, self.x)
        
        # return {
        #     "x_est": self.x_est,
        #     "x": self.x,
        # 
        # }

    def one_step(self, u: np.ndarray, L: np.ndarray):
        """
        Run one step of simulation
        """
        self.freq_model_system.one_step(u, L,  self.x_est, self.x)
        self.current_time += self.step_time
        self.next_time = self.current_time + self.step_time

        # return {
        #     "x_est": self.x_est,
        #     "x": self.x,
        # 
        # }


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog="freq_model_pyinterface",
        description="Python interface to freq_model.",
    )
    parser.add_argument("--stop_time", help="Simulation stop time. Total time of simulation.", type=float)
    parser.add_argument("--decimation", help="Decimation factor. Data is saved once every specified decimation factor time steps.", default=1, type=int)
    args = parser.parse_args()
    if args.stop_time is None:
        raise Exception("Stop time not specified. Type `python freq_model_pyinterface.py --help` for more info!!!")

    STEP_TIME = 0.02
    STOP_TIME = args.stop_time
    DECIMATION = args.decimation

    if STEP_TIME==-1:
        raise Exception("STEP_TIME not specified.")
    if STOP_TIME==-1:
        raise Exception("STOP_TIME not specified.")
    
    def to_numpy(*args):
        return np.array(args, dtype=np.float64)

    m = freq_model("freq_model_lib.so", step_time=STEP_TIME, compile=True)
    
    DATA_OUT = np.zeros((1+int(STOP_TIME/(STEP_TIME*DECIMATION)), 1+3 + 2), dtype=np.float64)

    # Specify value of input here
    # u = 
    # L = 
    
    m.reset(u, L)
    DATA_OUT[0,:] = to_numpy(m.current_time, m.x_est[0], m.x_est[1], m.x_est[2], m.x[0], m.x[1])
    
    LAST_CURRENT_TIME = m.current_time
    WALL_TIME_ORIGIN = time.time_ns()
    __counter__ = 0
    while m.current_time < STOP_TIME:
        # Specify value of input here
        # u = 
        # L = 
        

        m.one_step(u, L)
        __counter__ += 1

        if __counter__ % DECIMATION == 0:
            try:
                DATA_OUT[int(__counter__ / DECIMATION),:] = to_numpy(m.current_time, m.x_est[0], m.x_est[1], m.x_est[2], m.x[0], m.x[1])
            except:
                pass

        if (m.current_time - LAST_CURRENT_TIME) / STOP_TIME * 100 > 5:
            print(f"{round(m.current_time / STOP_TIME * 100, 0)}% complete. Total time elapsed: {(time.time_ns() - WALL_TIME_ORIGIN)/1e9} !!!")
            LAST_CURRENT_TIME = m.current_time

    if round(LAST_CURRENT_TIME / STOP_TIME * 100, 0)!=5:
        print(f"{round(100.0, 0)}% complete. Total time elapsed: {(time.time_ns() - WALL_TIME_ORIGIN)/1e9}!!!")
    hf = h5py.File("freq_model_out.h5", "w")
    hf.create_dataset("sim_out", data=DATA_OUT)
    hf.close()