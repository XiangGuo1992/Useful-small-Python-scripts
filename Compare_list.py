# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:50:43 2018

@author: Inki Kim's lab
"""


import os
path = 'G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\2.New Experiment\\videos'
path1 = 'G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\2.New Experiment\\4.analysis\\framepics'
path2 = 'G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\2.New Experiment\\4.analysis\\framepics_base'
file = os.listdir(path)
files1 = os.listdir(path1)
files2 = os.listdir(path2)
files = files1 + files2


for j in range(len(file)):
    file[j] = file[j].split('.')[0]






files_intersection = set(files1).intersection(files2)
#list the differences
list(set(file) - set(files))