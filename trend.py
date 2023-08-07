import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'F:/Pre_Thesis/poll_2017-2022.csv'
df = pd.read_csv(path)

df['Mean'] = df.iloc[:,1:6].mean(axis=1)
df['STD'] = df.iloc[:,1:6].std(axis = 1)

fig,ax  = plt.subplots(figsize = (14,7))

#ax1.invert_yaxis()
ax.axvspan(0, 58, color='skyblue', alpha=0.4)
ax.axvspan(58, 150, color='red', alpha=0.2)
ax.axvspan(150, 272, color='indigo', alpha=0.2)
ax.axvspan(272, 342, color='orange', alpha=0.3)
ax.axvspan(342, 364, color='skyblue', alpha=0.4)
ax.plot(df.index,df['Mean'],color = 'green',lw = 1.75,label = 'Mean')
ax.fill_between(df.index, df['Mean'] - df['STD'], df['Mean'] + df['STD'], alpha=0.5,color = 'green',label = 'SD')

ax.set_xticklabels([])
ax.set_ylabel('PM2.5 concentration (μg/m$^3$)', fontsize = 18)
ax.set_xlabel('Seasons', fontsize = 18)
ax.set_ylim([0,300])
ax.tick_params(axis = 'x',which='major', length=0, width=1.5, direction='inout')
ax.tick_params(axis = 'y',which='major', length=10, width=1.5, direction='inout')
ax.tick_params(axis='y', labelsize=15)
#ax.tick_params(axis='x', labelsize=12)
ax.tick_params(which='minor', length=0, width=0, direction='in')
plt.text(0.08, 0.8,'Winter', horizontalalignment='left',fontsize = 15,fontweight = 'bold',verticalalignment='center',transform = ax.transAxes)
plt.text(0.24, 0.8,'Pre-monsoon', horizontalalignment='left',fontsize = 15,fontweight = 'bold',verticalalignment='center',transform = ax.transAxes)
plt.text(0.52, 0.8,'Monsoon', horizontalalignment='left',fontsize = 15,fontweight = 'bold',verticalalignment='center',transform = ax.transAxes)
plt.text(0.735, 0.8,'Post-monsoon', horizontalalignment='left',fontsize = 15,fontweight = 'bold',verticalalignment='center',transform = ax.transAxes)
ax.legend(loc='upper right', fontsize=15)
#plt.savefig('F:/Pre_Thesis/trend.jpg',dpi = 300)
plt.show()