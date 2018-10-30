# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:45:37 2018

@author: Inki Kim's lab
"""

import os
import pandas as pd
import time


os.chdir('G:\\test_openpose\\input')  
for file in os.listdir():
    start = time.time()
    DF = pd.DataFrame()
    csv_files_path = os.path.join(os.getcwd(),file,'csvs')
    for i in os.listdir(csv_files_path):
        csv_file_path = csv_files_path + '\\' + i
        csv_file = pd.read_csv(csv_file_path)
        df = pd.DataFrame()
        df = df.append(csv_file.iloc[:,0:390])
        
        #body point
        for x in range(0,54,3):
            df.rename(columns={ df.columns[x]: 'pose_' + str(x//3)+'_x'}, inplace=True)
        for y in range(1,54,3):
            df.rename(columns={ df.columns[y]: 'pose_' + str(y//3)+'_y'}, inplace=True)
        for z in range(2,54,3):
            df.rename(columns={ df.columns[z]: 'pose_' + str(z//3)+'_score'}, inplace=True)
        
        #face point    
        for x1 in range(54,264,3):
            df.rename(columns={ df.columns[x1]: 'face_' + str((x1-54)//3)+'_x'}, inplace=True)
        for y1 in range(55,264,3):
            df.rename(columns={ df.columns[y1]: 'face_' + str((y1-54)//3)+'_y'}, inplace=True)
        for z1 in range(56,264,3):
            df.rename(columns={ df.columns[z1]: 'face_' + str((z1-54)//3)+'_score'}, inplace=True)
            
        #left hand point
        for x2 in range(264,327,3):
            df.rename(columns={ df.columns[x2]: 'Lefthand_' + str((x2-264)//3)+'_x'}, inplace=True)
        for y2 in range(265,327,3):
            df.rename(columns={ df.columns[y2]: 'Lefthand_' + str((y2-264)//3)+'_y'}, inplace=True)
        for z2 in range(266,327,3):
            df.rename(columns={ df.columns[z2]: 'Lefthand_' + str((z2-264)//3)+'_score'}, inplace=True) 
            
        #right hand point
        for x3 in range(327,390,3):
            df.rename(columns={ df.columns[x3]: 'Righthand_' + str((x3-327)//3)+'_x'}, inplace=True)
        for y3 in range(328,390,3):
            df.rename(columns={ df.columns[y3]: 'Righthand_' + str((y3-327)//3)+'_y'}, inplace=True)
        for z3 in range(329,390,3):
            df.rename(columns={ df.columns[z3]: 'Righthand_' + str((z3-327)//3)+'_score'}, inplace=True)
            
        namelist = ['people_' + str(i) for i in range(len(df))]
        df.insert(0, 'people', namelist)
        frame = i.split('-')[-1].split('_')[0].lstrip('0')
        df.insert(0, 'frame', frame)
        DF =DF.append(df)
    DF.to_csv('G:\\test_openpose\\output\\' + file + '.csv',index=False)
    print('%s output complete ' %file)
    end = time.time()
    print('time ellapsed is %d seconds\n ' %(end-start))
            
