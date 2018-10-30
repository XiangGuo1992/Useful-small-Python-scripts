# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:15:56 2018

@author: Xiang Guo
"""

import numpy as np
import cv2
import os
import glob
os.chdir('E:\\Xiang Guo\\JIGSAWS data\\Motion_History_Image')
videolist = glob.glob('*.avi')


for vid in videolist:
    path = 'E:\\Xiang Guo\\JIGSAWS data\\Motion_History_Image\\videos_frames\\' + vid.split('.')[0]  
    os.mkdir(path)
    vidcap = cv2.VideoCapture(vid)
    

    
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      filename = str("\\%d.jpg" % (count+1))
      filepath = path + filename
      cv2.imwrite(filepath, image)     # save frame as JPEG file
      count += 1