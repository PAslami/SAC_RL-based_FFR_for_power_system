# UTILS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

def plot_learning_curve(x, scores, fig_file):
    running_avg = np.zeros(len(scores))
    for i in range(len(running_avg)):
        running_avg[i] = np.mean(scores[max(0, i-10):(i+1)])
    plt.plot(x, running_avg)
    plt.title('Running average of previous 10 scores')
    if fig_file:
        plt.savefig(fig_file, dpi=600)
        print(f"Plot saved to {fig_file}")
    else:
        plt.show()

def new_mu(mu_init, n, new_obs):
    """
    Running mean reward.
    """
    return((n * mu_init + new_obs) / (n + 1))

def new_var(mu_init, var_init, mu_new, n, new_obs):
    """
    Running variance of the reward.
    """
    return(((n * var_init) / (n + 1))+(((new_obs - mu_new)**2) /n ))

def norm_reward(reward, mu_init, var_init, n):
    """
    Normalize the reward.

    Args:
        reward (float): The current reward to be normalized.
        mu_init (float): The current mean of the rewards.
        var_init (float): The current variance of the rewards.
        n (int): The count of rewards seen so far.

    Returns:
        norm_reward (float): The normalized reward.
        new_mu (float): Updated mean of the rewards.
        new_var (float): Updated variance of the rewards.
        new_n (int): Updated count of rewards seen.
    """
    if n ==0:
        new_mean = reward
        norm_reward = reward
        new_vari = var_init
    elif n ==1:
        new_mean = np.mean([mu_init, reward])
        new_vari = np.var([mu_init, reward])
        norm_reward = (reward-new_mean)/np.sqrt(new_vari*((n + 1) / n)) ###unbiased sigma
    else:
        new_mean = new_mu(mu_init, n, reward)
        new_vari = new_var(mu_init, var_init, new_mean, n, reward)
        norm_reward = (reward-new_mean)/np.sqrt(new_vari*((n + 1) / n))

    return norm_reward, new_mean, new_vari, n + 1

def setup_plot_fonts():
    rcParams.update({
        'font.family': 'serif',
        'font.size': 12,
        'lines.linewidth': 2
    })
    font = FontProperties(family='serif', size=12)
    return font

def plot_results(args, freq_no_ffr, freq_rl, freq_mpc, rocof_no_ffr, rocof_rl, rocof_mpc, input_power_rl, input_power_mpc, font= setup_plot_fonts(), fig_file = None):
    time = np.arange(0.0, args.stop_time+0.01, args.step_time)
    fig, ax = plt.subplots(1, 3, figsize=(14, 4), constrained_layout=True)
    # Plot frequency deviation
    ax[0].plot(time, freq_no_ffr, label="no FFR")
    ax[0].plot(time, freq_rl, label="SAC RL-based Control", color='C1')
    ax[0].plot(time, freq_mpc, label="MPC", color='C2')

    # for threshold, color, label in [
    #     (-0.0117, 'olive', 'UFLS T1: 59.3 Hz'),
    #     (-0.0183, 'blueviolet', 'UFLS T2: 58.9 Hz'),
    #     (-0.025, 'hotpink', 'UFLS T3: 58.5 Hz')
    # ]:
    #     ax[0].plot(time, np.full(len(time), threshold), label=label, color=color, linewidth=1.6, linestyle="--")

    ax[0].set_xlabel("time [s]", fontproperties=font)
    ax[0].set_ylabel("$\\Delta\\omega$ [pu]", fontproperties=font)
    ax[0].legend(loc=0, prop=font, labelspacing=0.2)
    ax[0].grid(True, linestyle="-.")

    # Plot rate of change of frequency (ROCOF)
    ax[1].plot(time, rocof_no_ffr, label="no FFR")
    ax[1].plot(time,  rocof_rl, label="SAC RL-based Control", color='C1')
    ax[1].plot(time, rocof_mpc, label="MPC", color='C2')

    ax[1].set_xlabel("time [s]", fontproperties=font)
    ax[1].set_ylabel("$\\dot{\\Delta\\omega}$ [pu]", fontproperties=font)
    ax[1].legend(loc=0, prop=font, labelspacing=0.2)
    ax[1].grid(True, linestyle="-.")

    # Plot inverter power injection
    ax[2].plot(time, input_power_rl, label="SAC RL-based Control", color='C1')
    ax[2].plot(time, input_power_mpc, label="MPC", color='C2')

    ax[2].set_xlabel("time [s]", fontproperties=font)
    ax[2].set_ylabel("$\\Delta P_{inv}$ [pu]", fontproperties=font)
    ax[2].legend(loc=0, prop=font, labelspacing=0.2)
    ax[2].grid(True, linestyle="-.")

    if fig_file:
        plt.savefig(fig_file, dpi=600)
        print(f"Plot saved to {fig_file}")
    else:
        plt.show()