import os
import numpy as np 
import sys
import nibabel as nib   
import time

class PrepHigh(object):
    def __init__(self,scan_name):
        self.scan_name  = scan_name
        self.T1_dir     = '/scratch/yangq6/learning/TractSeg/myData/input'
        self.tracts_dir = '/scratch/yangq6/learning/TractSeg/myData/output'
        self.detail_dir = '/scratch/yangq6/learning/TractSeg/doc/detail'
        self.detail_file     = os.path.join(self.detail_dir,scan_name+'.txt')

    def _io_check(self):
        if (os.path.isdir(os.path.join(self.T1_dir,self.scan_name)) and os.path.isdir(os.path.join(self.tracts_dir,self.scan_name)) and 
            os.path.isfile(self.detail_file)):
            print('*************************************')
            print('***********IO CHECK CORRECT**********')
            print('*************************************\n')
        else:
            ValueError("The directory/file doesn't exist")

    def _extract_ROI(self,input_file,output_file,index):
        x_index = [0, 24, 49, 73, 97]
        y_index = [0, 33, 66, 100,133]
        z_index = [0, 24, 49, 73, 97]

        cmd = 'fslroi {} {} {} 96 {} 96 {} 96'.format(input_file,output_file,x_index[index[0]],y_index[index[1]],z_index[index[2]])
        os.system(cmd)
        

    def _proc_files(self):
        # self._proc_T1()
        self._proc_tracts()

    def _proc_T1(self):
        T1_file = os.path.join(self.T1_dir,self.scan_name,'T1_max-{}.nii.gz'.format(self.scan_name))
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    prefix = str(i) + str(j) + str(k)
                    output_file = os.path.join(self.T1_dir,self.scan_name,'High_{}-T1_max-{}.nii.gz'.format(prefix,self.scan_name))

                    print('**********************************')
                    print('T1 index file is {}'.format(prefix))
                    print('**********************************\n')

                    self._extract_ROI(T1_file,output_file,[i,j,k])
        
    def _proc_tracts(self):
        Tracts_file = os.path.join(self.tracts_dir,self.scan_name,'Tracts_full.nii.gz')
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    prefix = str(i) + str(j) + str(k)

                    output_file = os.path.join(self.tracts_dir,scan_name,'High_{}-tracts-{}.nii.gz'.format(prefix,self.scan_name))
                    self._extract_ROI(Tracts_file,output_file,[i,j,k])

                    print('**********************************')
                    print('tracts index file is {}'.format(prefix))
                    print('**********************************\n')

                    self._binary_tracts(output_file)


    def _binary_tracts(self,output_file):
        detail_ID = np.loadtxt(self.detail_file,dtype=int,ndmin=1)
        
        img_nii   = nib.load(output_file)
        img       = img_nii.get_fdata()

        img[img >= 0.5] = 1
        img[img < 0.5 ] = 0

        if (detail_ID[0] > 0):
            for i in range(len(detail_ID)):
                img[:,:,:,detail_ID[i]] = img[:,:,:,detail_ID[i]] - 1
                print(detail_ID[i])
        else:
            print("No detail")

        img = img.astype(np.int8)

        bin_nii = nib.Nifti1Image(img,img_nii.affine,img_nii.header)
        bin_nii.header.set_data_dtype(np.int8)
        nib.save(bin_nii,output_file)

        print('*************************************************************')
        print('We binary the file {}'.format(os.path.basename(output_file)))
        print('*************************************************************\n')



    def Update(self):
        self._io_check()
        self._proc_files()


if __name__ == '__main__':
    scan_name = sys.argv[1]
    # scan_name = 'BLSA_0270_BLSA_0270_25-0_10'

    prep = PrepHigh(scan_name)
    prep.Update()



        