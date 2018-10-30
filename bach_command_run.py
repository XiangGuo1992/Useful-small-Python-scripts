# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:38:07 2018

@author: Xiang Guo
"""

import glob, os

'''
os.chdir('C:\\tensorflow-model\\models\\research\\object_detection\\protos')
for i in glob.glob("*.proto"):
    os.system('protoc {} --python_out=.'.format(i) )
    print (i)
'''
os.chdir('C:\\tensorflow-model\\models\\research\\object_detection\\protos\\')
for i in glob.glob("*.proto"):
    #os.system('protoc object_detection/protos/{}.proto --python_out=. '.format(i) )
    print ('protoc object_detection/protos/{} --python_out=. '.format(i) )