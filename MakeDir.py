import os

os.chdir('E:\\Xiang Guo\\JIGSAWS data\\Experimental_setup\\1_out_test\\test')

folders = os.listdir()
os.chdir('E:\\Xiang Guo\\JIGSAWS data\\Experimental_setup\\1_out_test\\MHI_test')

for i in folders:
    os.mkdir(i)

'''
for j in os.listdir():
    os.chdir('F:\\GuoXiang\\NoviceVideos\\Frames\\'+j)
    os.mkdir('Cut')
    os.mkdir('None')
    os.mkdir('Push_down')
    os.mkdir('tie_a_knot')
    os.mkdir('Transition')
'''