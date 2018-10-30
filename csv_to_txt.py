# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:53:37 2018

@author: Xiang Guo
"""
import csv
import os
os.chdir('G:\\Resource for Xiang\\Lian Cui experiment\\eyetracking data\\2.New Experiment\\4.analysis\\eyetracking\\2.Sycronized data')
filelist = os.listdir()

for file in filelist:
    with open(file,'r') as csv_file:
        csv_reader = csv.reader(csv_file) 
        newfile = file + '.txt'        
        for line in csv_reader:
            with open(newfile, 'a') as new_txt:    #new file has .txt extn
                txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                txt_writer.writerow(line)   #write the lines to file`