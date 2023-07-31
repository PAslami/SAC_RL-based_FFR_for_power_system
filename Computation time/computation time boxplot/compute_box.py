import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib import rcParams



plt.rcParams.update({'font.size': 12})
filename = pd.read_csv (r'computeRL.csv')    
table = pd.DataFrame(filename, columns= ['RL_opal_RT','MPC'])
l1= ["MPC"] * len(table.MPC)
l2 =["SAC RL-based FFR"] * len(table.RL_opal_RT)
data2 = {'Controller': l1+l2,'computation_period':table['MPC'].tolist()+table['RL_opal_RT'].tolist()}

df2 = pd.DataFrame(data2)

plt.figure(figsize=(6,3.9))
boxplot =sns.boxplot(data=df2, x="Controller", y="computation_period", width = 0.7)
plt.ylim([75,670])
plt.ylabel("computation time [$\mu$s]")
plt.grid(True, linestyle="-.")



medians = round(df2.groupby(['Controller'])['computation_period'].median(), 2)
vertical_offset = df2['computation_period'].median() * 0.08


for xtick in boxplot.get_xticks():
    boxplot.text(xtick,medians[xtick] + vertical_offset,medians[xtick], 
            horizontalalignment='center',size='large',color='r',weight='bold')
    boxplot.text(xtick+0.24,medians[xtick] + vertical_offset, "$\mu$s", 
            horizontalalignment='center',size='large',color='r',weight='bold')
    
plt.show()