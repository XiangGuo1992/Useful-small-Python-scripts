# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:08:33 2018

@author: Xiang Guo
"""

import glob
import moviepy.editor as mpy
import os
import re

os.chdir('E:\\Xiang Guo\\Lian\\test3')

gif_name = 'outputName'
fps = 30
file_list = glob.glob('*.jpg') # Get all the pngs in the current directory

ordered_file_list =sorted(file_list, key=lambda x: (int(re.sub('\D','',x)),x))


clip = mpy.ImageSequenceClip(ordered_file_list, fps=fps)
clip.write_videofile("E:\\Xiang Guo\\Lian\\ChrisV_lane2.mp4")