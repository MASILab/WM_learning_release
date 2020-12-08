import numpy as np
import os
import sys

class ParseDataFile(object):

    def __init__(self,data_file):
        self.data_file = data_file
        self._root = '/scratch/yangq6/learning/TractSeg/myData'

    def _parse_name(self):
        return os.path.basename(self.data_file).split('.')[0] + '.txt'

    def _parse_doc(self):

        txts = np.loadtxt(self.data_file,dtype=str)
        with open(self._parse_name(),'w') as f:
            for txt in txts:
                input,output = txt.strip().split(':')
                scan_name = os.path.basename(os.path.dirname(input))

                input_dir = os.path.join(self._root, 'input',  scan_name)
                output_dir = os.path.join(self._root,'output',scan_name)

                f.write('{}:{}\n'.format(input_dir,output_dir))

    def Update(self):
        self._parse_doc()


if __name__ == '__main__':
    doc_file = '../test_tractSeg.txt.bak'
    parse = ParseDataFile(doc_file)
    parse.Update()

