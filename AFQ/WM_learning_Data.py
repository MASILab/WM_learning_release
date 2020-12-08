import torch
import numpy as np
import nibabel as nib
from torch.utils.data import Dataset
import os

class dataset(Dataset):
    def __init__(self, data_file,type=None,tile_index =None,norm_type=None,norm_range=None):
        self.data_file = data_file
        self.type = type
        if (self.type == 'High'):
            self.norm_type  = "max"
            self.norm_range = None
            self.tile_index = tile_index

        if (self.type == 'low'):
            self.tile_index = None
            self.norm_type  = norm_type
            self.norm_range = norm_range

        self._proc_doc()

    def __len__(self):
        return self._data_txt.shape[0]

    def _proc_doc(self):
        self._data_txt = np.loadtxt(self.data_file,dtype=str)

    def _parse_doc(self,str):
        T1_folder, tract_folder = str.strip().split(':')
        self.scan_name = os.path.basename(T1_folder)

        return self._proc_T1_file(T1_folder), self._proc_tracts_file(tract_folder)

    def _proc_T1_file(self,T1_folder):
        if(self.type == "High"):
            T1_name = 'T1_{}-{}.nii.gz'.format(self.norm_type,self.scan_name)
            T1_file = os.path.join(T1_folder,T1_name)
            
        else:
            T1_name = 'T1_{}-{}-{}.nii.gz'.format(self.norm_type,self.scan_name,'img96')
            T1_file = os.path.join(T1_folder,T1_name)

        return T1_file


    def _proc_tracts_file(self,tract_folder):
        if (self.type == "High"):
            tracts_name = 'High_{}-tracts-{}.nii.gz'.format(self.tile_index,self.scan_name)
            tracts_file = os.path.join(tract_folder,tracts_name)

        else:
            tracts_name = '{}-{}.nii.gz'.format(scan_name,'bin96')
            tracts_file = os.path.join(tract_folder,tracts_name)

        return tracts_file



    def _proc_norm(self,t1):

        if self.norm_type == 'N3' and self.norm_range == '01':
            t1[t1 > 150] = 150
            t1 = t1 / 150 * 2 - 1

            return t1

        if self.norm_type != 'N3' and self.norm_range == '01':
            t1 = (t1 - torch.min(t1)) / (torch.max(t1) - torch.min(t1))

            return t1



    def _proc_T1(self,T1_file):
        t1 = torch.from_numpy(nib.load(T1_file).get_fdata()).type(torch.FloatTensor).unsqueeze(0)

        if (self.type == "High"):
            t1 = self._proc_T1_tile(t1)
            return t1

        return t1

    def _proc_T1_tile(self,t1):
        xz_index = [0, 24, 49, 73, 97]
        y_index = [0, 33, 66, 100,133]

        i = int(self.tile_index[0])
        j = int(self.tile_index[1])
        k = int(self.tile_index[2])


        t1 = t1[:,xz_index[i]:xz_index[i] + 96, y_index[j]:y_index[j] + 96, xz_index[k]:xz_index[k] + 96]

        return t1

    def _proc_tracts_tile(self,label):
        xz_index = [0, 24, 49, 73, 97]
        y_index = [0, 33, 66, 100,133]

        i = int(self.tile_index[0])
        j = int(self.tile_index[1])
        k = int(self.tile_index[2])


        label = label[xz_index[i]:xz_index[i] + 96, y_index[j]:y_index[j] + 96, xz_index[k]:xz_index[k] + 96,:]

        return label


    def _proc_tracts(self,tracts_file):
        labels = torch.from_numpy(nib.load(tracts_file).get_fdata()).type(torch.FloatTensor).squeeze(0)
        labels = labels.permute(3, 0, 1, 2)

        return labels


    def __getitem__(self, index):
        ind = index % self._data_txt.shape[0]
        T1_file, tracts_file = self._parse_doc(self._data_txt[ind])

        # print(T1_file)
        # print(tracts_file)

        t1 = self._proc_T1(T1_file)
        labels = self._proc_tracts(tracts_file)

        return {'t1':t1, 'labels':labels, 'nii_path':T1_file, 'out_paths':tracts_file}


if __name__ == '__main__':
    train_file = '../doc/train_reco.txt'
    data = dataset(train_file,type='High',tile_index ='123',norm_type='max',norm_range='00')
    print(torch.min(data[10]['labels'][0,:,:,:]))










