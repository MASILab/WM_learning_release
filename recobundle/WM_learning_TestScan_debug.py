import torch
import numpy as np
import nibabel as nib
import os
import sys
import logging
from WM_learning_Model import UNet3D
from WM_learning_ModelUtils import load_whichModel,load_model,save_nifti
from WM_learning_GetOption import get_test_option
from WM_learning_Data import dataset


def prepMerge(pred_dir,scan_name,t1_file):
    scan_dir = os.path.join(pred_dir,scan_name)
    tracts = os.listdir(scan_dir)
    tracts.sort()

    logFormatter = '%(asctime)s - %(message)s'
    logging.basicConfig(format=logFormatter, level=logging.INFO)
    logger = logging

    for i,tract in enumerate(tracts):
        logger.info('{} {}'.format(i,tract))
        tract_dir = os.path.join(scan_dir,tract)
        Merge1Tract(t1_file,tract_dir)


def Merge1Tract(T1_file,tract_dir):
    image = np.zeros([193,229,193])
    template = np.zeros([193,229,193])

    xz_index = [0, 24, 49, 73, 97]
    y_index = [0, 33, 66, 100,133]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                prefix = str(i)  +str(j) + str(k)
                tile_file = os.path.join(tract_dir,prefix + '_' + os.path.basename(tract_dir) + '.nii.gz')
                img = np.zeros([193,229,193])
                tmp = np.zeros([193,229,193])

                img[xz_index[i]:xz_index[i]+96,y_index[j]:y_index[j]+96,xz_index[k]:xz_index[k]+96] = nib.load(tile_file).get_fdata()
                tmp[xz_index[i]:xz_index[i]+96,y_index[j]:y_index[j]+96,xz_index[k]:xz_index[k]+96] = 1

                image += img
                template += tmp

    final = np.around(image/template,decimals=4).astype(np.float16)
    final[final<0.01] = 0
    save_path = os.path.join(os.path.dirname(tract_dir),os.path.basename(tract_dir) + '.nii.gz')
    save_nifti(final,save_path,T1_file)
    os.system('rm -rf {}'.format(tract_dir))


class TestScan(dataset):

    def __init__(self,tractID_file, options):
        self.tractID_file = tractID_file
        self.options= options
        self.norm_type = options.norm
        self.norm_range = options.range

        ## for data module parameters:
        self.type = options.type

        logFormatter = '%(asctime)s - %(message)s'
        logging.basicConfig(format=logFormatter, level=logging.INFO)
        self.logger = logging

    def Get_T1_file(self):
        return self._T1_file

    def Get_scan_name(self):
        return self.scan_name

    def SetIndex(self,index):
        self.ind = index

    def SetTile(self,index):
        self.tile_index = index

    def Update(self):
        self._proc_doc()
        # self._begin_low_Test()
        self._begin_High_test()

    def _proc_doc(self):
        txt = np.loadtxt(options.test_list,dtype=str)[self.ind]
        self._tractID = np.loadtxt(self.tractID_file,dtype=str)
        self._tractID = [tract +'.nii.gz' for tract in self._tractID]
        self.logger.info('The tract is {}'.format(self._tractID[0]))
        self._T1_file, tracts_file = self._parse_doc(txt)

    def _begin_low_Test(self):

        print('T1 file is {}'.format(self._T1_file))
        print('The model is {}'.format(load_whichModel(options.model_dir,options.model_prefix)))
        print('Save folder is {}'.format(options.folder))

        model = UNet3D(1,72)
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda" if use_cuda else "cpu")
        model = model.to(device)

        model = load_model(model,load_whichModel(options.model_dir,options.model_prefix))
        model.eval()

        os.mkdir(os.path.join(options.folder,self.scan_name))

        with torch.no_grad():
            output = model(self._proc_T1(self._T1_file).unsqueeze(0).to(device))
            output = torch.nn.Sigmoid()(output)
            for i in range(output.shape[1]):
                save_path = os.path.join(options.folder,self.scan_name,self._tractID[i])
                img = np.around(output[0,i,:,:,:].cpu().detach().numpy(),decimals=4).astype(np.float16)
                img[img < 0.01] = 0
                save_nifti(img,save_path,self._T1_file)

    def _begin_High_test(self):
        self.logger.info('T1 file is {}'.format(self._T1_file))
        self.logger.info('The model is {}'.format(load_whichModel('{}-'.format(self.tile_index))))
        self.logger.info('Save folder is {}'.format(options.folder))
        self.logger.info('test tile index is {}'.format(self.tile_index))
        self._proc_T1(self._T1_file)

        model = UNet3D(1,44)
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda" if use_cuda else "cpu")
        model = model.to(device)

        model = load_model(model,load_whichModel('{}-'.format(self.tile_index))[0])
        model.eval()

        if (not os.path.isdir(os.path.join(options.folder,self.scan_name))):
            os.mkdir(os.path.join(options.folder,self.scan_name))

        with torch.no_grad():
            output = model(self._proc_T1(self._T1_file).unsqueeze(0).to(device))
            output = torch.nn.Sigmoid()(output)
            for i in range(output.shape[1]):
                save_tract_dir = os.path.join(options.folder,self.scan_name,self._tractID[i].split('.')[0]) 
                if (not os.path.isdir(save_tract_dir)):
                    os.mkdir(save_tract_dir)
                save_path = os.path.join(save_tract_dir,self.tile_index + '_' + self._tractID[i])
                img = np.around(output[0,i,:,:,:].cpu().detach().numpy(),decimals=4).astype(np.float16)
                img[img < 0.01] = 0
                save_nifti(img,save_path,self._T1_file)


    @classmethod
    def toInt(cls,string):
        return int(string)


if __name__ == '__main__':
    scan_index = TestScan.toInt(sys.argv[1])
    options = get_test_option()

    logFormatter = '%(asctime)s - %(message)s'
    logging.basicConfig(format=logFormatter, level=logging.INFO)
    logger = logging

    logger.info('********************************')
    logger.info('we need to print the option')
    logger.info(options)
    logger.info('********************************')

    tractID_file = '/scratch/yangq6/learning/Recobundle/doc/recoID.txt'

    testScan = TestScan(tractID_file,options)
    testScan.SetIndex(scan_index)

    for i in range(5):
        for j in range(5):
            for k in range(5):
                tile = str(i) + str(j) + str(k)
                testScan.SetTile(tile)
                testScan.Update()

    prepMerge('../pred',testScan.Get_scan_name(),testScan.Get_T1_file())

    

    
        



























