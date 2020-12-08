import os
import numpy as np

def DelData():
    data_dir = '/scratch/yangq6/learning/Recobundle/myData/output'
    subj_lists = sorted(os.listdir(data_dir))
    for subj in subj_lists:
        subj_dir = os.path.join(data_dir,subj)
        cmd = 'rm -rf {}/High*'.format(subj_dir)
        print(cmd)
        os.system(cmd)

def CheckData():
    data_dir = '/scratch/yangq6/learning/AFQ/myData/output'
    subj_lists = sorted(os.listdir(data_dir))
    for i,subj in enumerate(subj_lists):
        print(i)
        subj_dir = os.path.join(data_dir,subj)
        # print(len(os.listdir(subj_dir)))

        if (not len(os.listdir(subj_dir)) == 127):
            print(subj)


if __name__ == '__main__':
    CheckData()
    
    