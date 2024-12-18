"""
Filename:       test_compute_time.py
Written by:     Pooja Aslami
"""
import os
from sacFFR import DATA_DIR
from sacFFR.Evaluate.compute_time import get_inpt_args, plot_computation_time_boxplot

def test_compute_time():
    args = get_inpt_args()
    args.fig_file = "compute_time.png"
    filepath = os.path.join(DATA_DIR, "compute_time", "compute_time.csv")  ### path to csv file with computational time data
    plot_computation_time_boxplot(filepath, fig_file = args.fig_file)

if __name__ == "__main__":
    test_compute_time()