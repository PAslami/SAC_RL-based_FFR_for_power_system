"""
Filename:       test_policy.py
Written by:     Pooja Aslami
"""
import torch as T
import numpy as np
import h5py
import os
import sys
from sacFFR.Environments.Grid import Freq_Dynamics  
from sacFFR.Train.sac_modules.sac_parser import create_parser 
from sacFFR.Train.sac_modules.utils import plot_results
from sacFFR import SACFFR_DIR, DATA_DIR
sys.path.append(os.path.join(SACFFR_DIR, "Train", "sac_modules"))   

def get_inpt_args():
    parser = create_parser()
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print(f"[RLFDI WARNING]: {unknown} unknown argument(s)")
    return args

def load_mpc_data(data_dir, filename, variable):
    filepath = os.path.join(data_dir, "MPC_data", filename)

    with h5py.File(filepath, 'r') as file:
        return file[variable][()]
def initialize_environment(args, policy_path):
    env = Freq_Dynamics(
        Q11=args.Q1,
        Q22=args.Q2,
        R11=args.R1,
        reset_time=args.reset_time,
        stop_time=args.stop_time,
        load_range=[-args.load_range, args.load_range],
        compile=False,
        train=args.train,
        test_load=args.test_load
    )
    model = T.load(policy_path)
    return env, model


def simulate(env, model, apply_rl_control=True):
    state_log, input_power_log, frequency_state  = [], [], []
    prev_state = env.reset()
    done = False
    while not done:
        prev_state_tensor = T.Tensor([prev_state])
        if apply_rl_control:
            action, _ = model(prev_state_tensor)
            action = T.tanh(action) * 0.5
            action = action.cpu().detach().numpy()[0]
        else:
            action = 0.0

        observation, _, done, _ = env.step(np.array([action]))
        prev_state = observation
        state_log.append(observation)
        input_power_log.append(action)
        frequency_state.append(observation[0])

    return state_log, input_power_log, frequency_state

def print_statis(freq_no_ffr, freq_rl, freq_mpc, input_power_rl, input_power_mpc):
    improvement_rl = (max(abs(np.array(freq_no_ffr)))- max(abs(np.array(freq_rl))))*100/ max(abs(np.array(freq_no_ffr)))
    improvement_mpc = (max(abs(np.array(freq_no_ffr)))- max(abs(np.array(freq_mpc))))*100/ max(abs(np.array(freq_no_ffr)))
    # Print statistics
    print(f'Nadir no FFR: {max(abs(np.array(freq_no_ffr))):.3f}')
    print(f'Nadir RL: {max(abs(np.array(freq_rl))):.3f}')
    print(f'Nadir MPC: {max(abs(freq_mpc)):.3f}')
    print(f'Peak Power RL: {max(abs(np.array(input_power_rl)))[0]:.3f}')
    print(f'Peak Power MPC: {max(abs(input_power_mpc)):.3f}')
    print(f"Improvement RL: {improvement_rl:.2f}%")
    print(f"Improvement MPC: {improvement_mpc:.2f}%")
    return 


if __name__ == "__main__":
    args = get_inpt_args()
    args.train = False
    args.test_load = 0.44  ### define test load here
    # Load mpc data
    mpc_data = load_mpc_data(DATA_DIR, "mpcL0pt44.mat", "datavar")  ### loading corresponding mpc file 

    # Initialize environment and model
    policy_path = os.path.join(DATA_DIR,"trained_sac", "norm_Actormodel_11_8_epi3550")  ### path of trained agent
    env, model = initialize_environment(args, policy_path)

    # Simulate no FFR, RL control, and MPC
    states_no_ffr, _, freq_no_ffr = simulate(env, model, apply_rl_control=False)
    states_rl, input_power_rl, freq_rl = simulate(env, model, apply_rl_control=True)
    
    # Data extraction
    freq_no_ffr= [states_no_ffr[k][0] for k in range(len(states_no_ffr))]
    freq_rl= [states_rl[k][0] for k in range(len(states_rl))]
    freq_mpc = mpc_data[:, 3]

    rocof_no_ffr= [states_no_ffr[k][1] for k in range(len(states_no_ffr))]
    rocof_rl= [states_rl[k][1] for k in range(len(states_rl))]
    rocof_mpc = mpc_data[:, 4]

    input_power_mpc = mpc_data[:, 5]

    # print statistics
    print_statis(freq_no_ffr, freq_rl, freq_mpc, input_power_rl, input_power_mpc)

    # Plot results
    plot_results(args, freq_no_ffr, freq_rl, freq_mpc, rocof_no_ffr, rocof_rl, rocof_mpc, input_power_rl, input_power_mpc, fig_file =args.fig_file)