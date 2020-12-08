import os
import numpy as np
import nibabel as nib 
import torch
import sys

from WM_learning_Model import UNet3D
from WM_learning_ModelUtils import load_whichModel,load_model,save_nifti
from WM_learning_GetOption import get_test_option
from WM_learning_Data import dataset

class TestScan(dataset):
     
    def __init__(self,scan_index,ID_file,options):
        self.options = options  
        self.type = options.type
        self.scan_index = scan_index
        self.ID_file = ID_file
        self._init()

    def _init(self):
        self._final_img = np.zeros([44,193,229,193])
        self._count_img = np.zeros([193,229,193])
        self._tracts_ID = np.loadtxt(ID_file,dtype=str)
        txt = np.loadtxt(self.options.test_list,dtype=str)[self.scan_index]
        #! do following step for dataset class
        self.norm_type = options.norm
        self.norm_range = options.range


        #! Set tile index to run dataset module
        self.tile_index='555'
        self._T1_file,tract_file = self._parse_doc(txt)
        #! make dir for one scan
        print(self.scan_name)
        os.mkdir(os.path.join(self.options.folder,self.scan_name))

    def _save(self):
        save_nii = nib.load(self._T1_file)
        tracts = self._final_img.shape[3]
        for i in range(tracts):
            save_path = os.path.join(self.options.folder,self.scan_name,'{}.nii.gz'.format(tracts[i]))
            save_img = np.around(self._final_img[:,:,:,i]/self._count_img,decimals=3)
            save_nifti(save_img,save_path,self._T1_file)
        
    def Update(self):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    index = str(i) + str(j) + str(k)
                    self.tile_index = index
                    self._begin_High_test()

        self._save()

    def _begin_High_test(self):
        print('T1 file is {}'.format(self._T1_file))
        print('The model is {}'.format(load_whichModel('{}-'.format(self.tile_index))[0]))
        print('Save folder is {}'.format(options.folder))
        print('test tile index is {}'.format(self.tile_index))
        self._proc_T1(self._T1_file)

        model = UNet3D(1,44)
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda" if use_cuda else "cpu")
        model = model.to(device)

        model = load_model(model,load_whichModel('{}-'.format(self.tile_index))[0])
        model.eval()

        with torch.no_grad():
            output = model(self._proc_T1(self._T1_file).unsqueeze(0).to(device))
            output = torch.nn.Sigmoid()(output)
            img = np.around(output[0,:,:,:,:].cpu().detach().numpy(),decimals=4).astype(np.float16)
            img[img < 0.01] = 0
            self._merge_img(img,self.tile_index)

    def _merge_img(self,img,index):
        xz_index = [0, 24, 49, 73, 97]
        y_index  = [0, 33, 66, 100,133]
        index = [int(ind) for ind in index]
        self._final_img[:,
                        xz_index[index[0]]:xz_index[index[0]]+96,
                         y_index[index[1]]: y_index[index[1]]+96,
                        xz_index[index[2]]:xz_index[index[2]]+96] += img

        self._count_img[xz_index[index[0]]:xz_index[index[0]]+96,
                         y_index[index[1]]: y_index[index[1]]+96,
                        xz_index[index[2]]:xz_index[index[2]]+96] += 1


        
if __name__ == '__main__':
    scan_index = int(sys.argv[1])
    ID_file = '/scratch/yangq6/learning/Recobundle/doc/recoID.txt'
    options = get_test_option()

    print('********************************')
    print('we need to print the option')
    print(options)
    print('********************************')

    testscan = TestScan(scan_index,ID_file,options)
    testscan.Update()


