"""
Filename:       test_policy.py
Written by:     Pooja Aslami
"""
import torch as T
import numpy as np
import h5py
import os
import sys
import matplotlib.pyplot as plt
from sacFFR.Environments.Grid import Freq_Dynamics  
from sacFFR.Train.sac_modules.sac_parser import create_parser 
from sacFFR.Train.sac_modules.utils import setup_plot_fonts
from sacFFR import SACFFR_DIR, DATA_DIR
sys.path.append(os.path.join(SACFFR_DIR, "Train", "sac_modules"))   
prefix = "mpcL"
variable = "datavar"
def get_inpt_args():
    parser = create_parser()
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print(f"[RLFDI WARNING]: {unknown} unknown argument(s)")
    return args


def load_mpc_data(step_load_low=0.00, step_load_high=0.61, step_load_gap=0.02):
    Data_mpc = []
    for n, L in enumerate(np.arange(step_load_low, step_load_high, step_load_gap), start=0):  # Start count from 1
        mat_file = f"{prefix}{str(round(L, 2)).replace('.', 'pt')}.mat"
        filename = os.path.join(DATA_DIR,"MPC_data", mat_file)
        with h5py.File(filename, 'r') as file:
            Data_mpc.append(file[variable][()])
        tk = (Data_mpc[n][:,0] >= 0) & (Data_mpc[n][:,0]<=np.inf)
        Data_mpc[n] = Data_mpc[n][tk, :]
    return Data_mpc

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

def simulate(env, model, step_load_low=0.00, step_load_high=0.61, step_load_gap=0.02,apply_rl_control=True):
    Data_rl= []
    for L in np.arange(step_load_low, step_load_high, step_load_gap):
        state_log = []
        env.test_load = round(L, 2)
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
        Data_rl.append(state_log)
    return Data_rl


def calculate_metric(data_mpc, data_rl, data_no_ffr, step_load_low=0.00, step_load_high=0.61, step_load_gap=0.02, metric_type="nadir"):
    def extract_min(data, idx):  # Helper function to extract minimums
        return [min([state[idx] for state in state_log]) for state_log in data]

    result_mpc = []
    idx_map = {"nadir": (1, 3, 0), "rocof_pt": (3, 1, 1)}  # Mapping for indices
    idx1, idx2, rl_idx = idx_map[metric_type]
    # print(idx1, idx2, rl_idx)
    
    result_rl = extract_min(data_rl, rl_idx)
    result_no_ffr = extract_min(data_no_ffr, rl_idx)

    for n, L in enumerate(np.arange(step_load_low, step_load_high, step_load_gap)):
        result_mpc.append(min(data_mpc[n][:, idx1 if -0.2 <= L <= 0.2 else idx2]))

    return result_mpc, result_rl, result_no_ffr

def plot_nadir(data_mpc, data_rl, data_no_ffr,step_load_low=0.00, step_load_high=0.61, step_load_gap=0.02,  metric_type="nadir", fig_file = None):
    font = setup_plot_fonts()
    x_values = np.arange(step_load_low, step_load_high, step_load_gap)
    fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)
    # Plot the data for metric_type with different configurations
    ax.plot(x_values, np.array(data_no_ffr), '-o', markersize=4, label=f'{metric_type} - no FFR', color='C0')
    ax.plot(x_values, np.array(data_rl), '--bo', markersize=4, label=f'{metric_type} - SAC RL-based FFR', color='C1')
    ax.plot(x_values, np.array(data_mpc), '--bo', markersize=4, label=f'{metric_type} - MPC', color='C2')

    # Plot UFLS thresholds
    for threshold, color, label in [
        (-0.0117, 'olive', 'UFLS T1: 59.3 Hz'),
        (-0.0183, 'blueviolet', 'UFLS T2: 58.9 Hz'),
        (-0.025, 'hotpink', 'UFLS T3: 58.5 Hz')
    ]:
        ax.plot(x_values, np.full(len(x_values), threshold), label=label, color=color, linewidth=1.6, linestyle="--")

    # Vertical line at x=0
    ax.axvline(x=0.0, color='black', linestyle='--', linewidth=0.5)
    ax.grid(True, linestyle="-.")
    ax.set_xlabel('Load change $\Delta P_{inv}$ [pu]', fontproperties=font)
    ax.set_ylabel(f'{metric_type} of $\Delta \omega$ [pu]', fontproperties=font)
    ax.legend(loc=3, prop=font, fontsize=12)
    if fig_file:
        plt.savefig(fig_file, dpi=600)
        print(f"Plot saved to {fig_file}")
    else:
        plt.show()


if __name__ == "__main__":
    args = get_inpt_args()
    args.train = False

    # Initialize environment and model
    policy_path = os.path.join(DATA_DIR,"trained_sac", "norm_Actormodel_11_8_epi3550")  ### path of trained agent
    env, model = initialize_environment(args, policy_path)
    # Simulate no FFR, RL control, and MPC over step load range 
    data_mpc = load_mpc_data()
    data_rl = simulate(env, model, apply_rl_control=True)
    data_no_ffr = simulate(env, model, apply_rl_control=False)

    # obtain particular metic data
    data_mpc, data_rl, data_no_ffr= calculate_metric(data_mpc, data_rl, data_no_ffr, metric_type="nadir")

    # Plot results
    print(f"file to save {args.fig_file}")
    plot_nadir(data_mpc, data_rl, data_no_ffr, metric_type="nadir", fig_file =args.fig_file)