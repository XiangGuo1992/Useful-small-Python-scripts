# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:57:42 2018

@author: Xiang Guo
"""

import os
os.chdir('G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\DeepLearning_analysis\\output2\\pics')

for file in os.listdir():    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    name = file.replace('Lane ', 'Lane')   #去掉空格
    #name = file.title()
    os.rename(file, name)

