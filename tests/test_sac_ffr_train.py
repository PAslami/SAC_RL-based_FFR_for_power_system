"""
Filename:       test_sac_ffr_train.py
Written by:     Pooja Aslami
"""
from sacFFR.Train.sac_ffr_train import get_inpt_args, setup_env_agent, train

def test_sac_ffr_train():
    args = get_inpt_args()
    args.train = True
    args.n_episodes = 1
    args.fig_file = "train_reward.png"
    # args.load_checkpoint = True
    env, agent = setup_env_agent(args)
    train(args, env, agent)

if __name__ == "__main__":
    test_sac_ffr_train()