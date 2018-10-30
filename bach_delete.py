# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:24:31 2018

@author: Inki Kim's lab
"""
#remove the file with largest frame number
import os
import re
os.chdir('G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\2.New Experiment\\4.analysis\\framepics_base')

for file in os.listdir():    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    subdir = os.path.join(os.getcwd(),file)
    
    indexes =[int(re.findall("\d+",x)[0]) for x in os.listdir(subdir)]
    indexes.sort()
    name = 'frame' + str(indexes[-1]) + '.jpg'
    filedir = subdir + '\\' + name
    os.remove(filedir)