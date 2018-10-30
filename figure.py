# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:03:30 2018

@author: Xiang Guo
"""

## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 
import pandas as pd
import os
import matplotlib.pyplot as plt 

os.chdir('C:\\Users\\Xiang Guo\\OneDrive\\HFES2018\\7_figures')

PRC = pd.read_excel('AOI_vehicle.xlsx')


labels = ['0.6s','0.8s', '1.0s','1.2s','1.4s']



THW06 = PRC['AOI_percent'][PRC['headway']==0.6]
THW08 = PRC['AOI_percent'][PRC['headway']==0.8]
THW10 = PRC['AOI_percent'][PRC['headway']==1]
THW12 = PRC['AOI_percent'][PRC['headway']==1.2]
THW14 = PRC['AOI_percent'][PRC['headway']==1.4]

## combine these different collections into a list    
data_to_plot = [THW06, THW08, THW10, THW12, THW14]

plt.figure()

plt.boxplot(data_to_plot,labels=labels,showmeans=True)

plt.title('Percent of dwelling time at leading vehicle vs. Time Headway', fontsize=10)

#plt.xticks([1, 2, 3,4,5], ['0.6', '0.8', '1.0', '1.2','1.4'])

plt.savefig("AOI_vehicle.png")




