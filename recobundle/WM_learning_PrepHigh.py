import os
import numpy as np 
import sys
import nibabel as nib   
import time
import logging



class PrepHigh(object):

    
    def __init__(self,scan_name):
        self.scan_name  = scan_name
        self.tracts_dir = '/scratch/yangq6/learning/Recobundle/myData/output'
        self.detail_dir = '/scratch/yangq6/learning/Recobundle/doc/detail'
        self.detail_file     = os.path.join(self.detail_dir,scan_name+'.txt')

        logFormatter = '%(asctime)s - %(message)s'
        logging.basicConfig(format=logFormatter, level=logging.INFO)

        self.logger = logging

    def _io_check(self):
        if os.path.isdir(os.path.join(self.tracts_dir,self.scan_name)) and os.path.isfile(os.path.join(self.tracts_dir,self.scan_name,'{}_bin.nii.gz'.format(self.scan_name))):
            self.logger.info('*************************************')
            self.logger.info('***********IO CHECK CORRECT**********')
            self.logger.info('*************************************\n')
        else:
            raise ValueError("The directory/file doesn't exist {}".format(os.path.join(self.tracts_dir,self.scan_name,'{}_full.nii.gz'.format(self.scan_name))))

    def _extract_ROI(self,input_file,output_file,index):
        x_index = [0, 24, 49, 73, 97]
        y_index = [0, 33, 66, 100,133]
        z_index = [0, 24, 49, 73, 97]

        cmd = 'fslroi {} {} {} 96 {} 96 {} 96'.format(input_file,output_file,x_index[index[0]],y_index[index[1]],z_index[index[2]])
        os.system(cmd)
        

    def _proc_files(self):
        self._proc_tracts()
        
    def _proc_tracts(self):
        Tracts_file = os.path.join(self.tracts_dir,self.scan_name,'{}_bin.nii.gz'.format(self.scan_name))
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    prefix = str(i) + str(j) + str(k)

                    output_file = os.path.join(self.tracts_dir,scan_name,'High_{}-tracts-{}.nii.gz'.format(prefix,self.scan_name))
                    self._extract_ROI(Tracts_file,output_file,[i,j,k])

                    self.logger.info("The split tract file is {}".format(Tracts_file))
                    self.logger.info('**********************************')
                    self.logger.info('tracts index file is {}'.format(prefix))
                    self.logger.info('output file is {}'.format(output_file))
                    self.logger.info('**********************************\n')

                    self._binary_tracts(output_file)


    def _binary_tracts(self,output_file):
        # detail_ID = np.loadtxt(self.detail_file,dtype=int,ndmin=1)
        
        img_nii   = nib.load(output_file)
        img       = img_nii.get_fdata()


        img = img.astype(np.int8)

        bin_nii = nib.Nifti1Image(img,img_nii.affine,img_nii.header)
        bin_nii.header.set_data_dtype(np.int8)
        nib.save(bin_nii,output_file)

        self.logger.info('*************************************************************')
        self.logger.info('We binary the file {}'.format(os.path.basename(output_file)))
        self.logger.info('*************************************************************\n')


    def Update(self):
        self._io_check()
        self._proc_files()

if __name__ == '__main__':
    scan_name = sys.argv[1]
    # scan_name = 'BLSA_0270_BLSA_0270_25-0_10'

    prep = PrepHigh(scan_name)
    prep.Update()



        