"""
Filename:       test_multi_step_load_eval.py
Written by:     Pooja Aslami
"""
import os
from sacFFR import DATA_DIR
from sacFFR.Evaluate.multi_step_load_eval import get_inpt_args, load_mpc_data, initialize_environment, simulate, calculate_metric, plot_nadir

def test_multi_step_load_eval():
    args = get_inpt_args()
    args.train = False
    args.fig_file = "multi_step_load_eval.png"
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

if __name__ == "__main__":
    test_multi_step_load_eval()