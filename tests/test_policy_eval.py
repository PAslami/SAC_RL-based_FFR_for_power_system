"""
Filename:       test_policy_eval.py
Written by:     Pooja Aslami
"""
import os
from sacFFR import DATA_DIR
from sacFFR.Train.sac_modules.utils import plot_results
from sacFFR.Evaluate.policy_eval import get_inpt_args, load_mpc_data, initialize_environment, simulate, print_statis

def test_policy_eval():
    args = get_inpt_args()
    args.train = False
    args.test_load = 0.44  ### define test load here
    args.fig_file = "policy_eval.png"
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

if __name__ == "__main__":
    test_policy_eval()