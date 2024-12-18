import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib import rcParams
from sacFFR import DATA_DIR
import os
from sacFFR.Train.sac_modules.sac_parser import create_parser
from sacFFR.Train.sac_modules.utils import setup_plot_fonts

def get_inpt_args():
    parser = create_parser()
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print(f"[RLFDI WARNING]: {unknown} unknown argument(s)")
    return args
def plot_computation_time_boxplot(filepath, fig_file = None):
    font = setup_plot_fonts()
    File = pd.read_csv(filepath)
    table = pd.DataFrame(File, columns=['RL_opal_RT', 'MPC'])
    l1 = ["MPC"] * len(table.MPC)
    l2 = ["SAC RL-based FFR"] * len(table.RL_opal_RT)
    data = {'Controller': l1 + l2, 'computation_period': table['MPC'].tolist() + table['RL_opal_RT'].tolist()}
    df = pd.DataFrame(data)
    # Set figure size
    plt.figure(figsize=(6, 3.9))
    
    # Create the boxplot

    boxplot = sns.boxplot(data=df, x="Controller", y="computation_period", width=0.7)
    plt.ylim([75, 670])
    plt.ylabel("Computation time [$\mu$s]", fontproperties=font)
    plt.grid(True, linestyle="-.")
    
    # Calculate and annotate the median
    medians = round(df.groupby(['Controller'])['computation_period'].median(), 2)
    vertical_offset = df['computation_period'].median() * 0.08

    for xtick in boxplot.get_xticks():
        boxplot.text(xtick, medians[xtick] + vertical_offset, medians[xtick], 
                     horizontalalignment='center', size='large', color='r', weight='bold')
        boxplot.text(xtick + 0.24, medians[xtick] + vertical_offset, "$\mu$s", 
                     horizontalalignment='center', size='large', color='r', weight='bold')
    if fig_file:
        plt.savefig(fig_file, dpi=600)
        print(f"Plot saved to {fig_file}")
    else:
        plt.show()

if __name__ == "__main__":
    args = get_inpt_args()
    filepath = os.path.join(DATA_DIR, "compute_time", "compute_time.csv")  ### path to csv file with computational time data
    plot_computation_time_boxplot(filepath, fig_file = args.fig_file)