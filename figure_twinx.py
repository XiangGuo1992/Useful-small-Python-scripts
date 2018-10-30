# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:01:01 2018

@author: Xiang Guo
"""

import numpy as np 

import pandas as pd
import os
import matplotlib.pyplot as plt 


os.chdir('C:\\Users\\Xiang Guo\\OneDrive\\HFES2018\\7_figures')

PRC_AOI_fixation = pd.read_excel('Vehicle_AOI_fixation.xlsx')

x = [0.6, 0.8, 1.0 ,1.2, 1.4]
y1=[]  #fixation times
y2 = []    #average fixation
error1 = []
error2 = []
for i in x:
    THW = PRC_AOI_fixation['EntryTimeCount'][PRC_AOI_fixation['headway'] == i]
    THW2 = PRC_AOI_fixation['in_AOI_time_average'][PRC_AOI_fixation['headway'] == i]
    y1.append(np.mean(THW))
    error1.append(np.std(THW)/np.sqrt(len(THW)))
    y2.append(np.mean(THW2))
    error2.append(np.std(THW2)/np.sqrt(len(THW2)))
    


labels = ['0.6s','0.8s', '1.0s','1.2s','1.4s']


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel('Number of fixation times', fontsize= 15)
ax1.set_title("Leading Vehicle AOI vs. Time Headway")

ax1.bar(labels, y1, yerr=error1,  alpha=0.5,color ='blue',label = 'Number of fixation times')
ax1.legend(['Number of fixation times'],loc='upper left',numpoints=1, fancybox=True,fontsize=10.5)



#align='center',

ax2 = ax1.twinx() 

ax2.plot(labels, y2, linewidth = 2, color ='orange')
ax2.errorbar(labels, y2, yerr=error2,  fmt='o',  color ='orange')

ax2.set_ylim(0,1)

ax2.legend(['Average fixation time'],loc='upper right',numpoints=1, fancybox=True,fontsize=10.5)


ax2.set_ylabel('Average fixation time(s)', fontsize= 15)
ax2.set_xlabel('Same X for both exp(-x) and ln(x)')

plt.savefig("Vehicle_AOI_fixation.png")






