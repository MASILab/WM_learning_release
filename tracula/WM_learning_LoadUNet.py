import torch
from WM_learning_ModelUtils import load_checkpoint, load_whichModel
from WM_learning_Model import UNet3D
from WM_learning_GetBasicPara import BasicPara

class LoadUnet(object):
    def __init__(self,options,device):
        self.options = options
        self.device = device

    def Load(self):
        if(self.options.scratch == True):
            print("we begin to learn from scratch")
            return self._learnScratch()
        else:
            print("we begin to learn based on transfer learning")
            return self._learnTransfer()

    def _learnTransfer(self):
        index = self.options.index
        para = BasicPara()
        para.Update()
        learnFrom = para.Get_transfer_dict()[index]
        
        model = UNet3D(1,18)

        model,optimizer  = model.to(self.device), torch.optim.Adam(model.parameters(), lr=0.0001)
        model_path,epoch = load_whichModel(learnFrom)

        print('the model we want to load {}'.format(model_path))

        model,optimizer  = load_checkpoint(model,optimizer,model_path)

        if(learnFrom == self.options.index):
            self.options.start_epoch = epoch + 1

        return model,optimizer


    def _learnScratch(self):

        model = UNet3D(1,18)

        model,optimizer = model.to(self.device), torch.optim.Adam(model.parameters(), lr=0.0001)

        return model,optimizer

if __name__=='__main__':
    pass

