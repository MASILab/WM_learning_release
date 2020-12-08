import os 
import numpy as np 

def format(data_file,type):
    doc_dir = '/scratch/yangq6/learning/Xtract/doc'
    reco_tract_dir = '/scratch/yangq6/learning/Xtract/myData/output'
    data_list = np.loadtxt(data_file,dtype=str)
    with open(os.path.join(doc_dir,'{}_xtract.txt'.format(type)),'w') as f:
        for data in data_list:
            T1, tract = data.split(':')
            subj = os.path.basename(T1)
            tract_dir = os.path.join(reco_tract_dir,subj)
            if (os.path.isdir(os.path.join(reco_tract_dir,subj))):
                # print(tract_dir)
                f.write('{}:{}\n'.format(T1,tract_dir))

if __name__ == '__main__':
    data_file = '/scratch/yangq6/learning/TractSeg/doc/valid_tractSeg_HaveSkull.txt'
    type = 'valid'
    format(data_file,type)

    data_file = '/scratch/yangq6/learning/TractSeg/doc/test_tractSeg_HaveSkull.txt'
    type = 'test'
    format(data_file,type)

    data_file = '/scratch/yangq6/learning/TractSeg/doc/train_tractSeg_HaveSkull.txt'
    type = 'train'
    format(data_file,type)



