import torch
import os
from torch.utils.data import DataLoader
from WM_learning_Data import dataset
from WM_learning_ModelUtils import train, valid, save_model, load_model, load_checkpoint, load_whichModel
from WM_learning_GetOption import get_train_option
from WM_learning_LoadUNet import  LoadUnet
from WM_learning_ProcDoc import open_doc,write_doc
import logging 


def train_model(options):
    use_cuda = torch.cuda.is_available()
    torch.manual_seed(1)
    device = torch.device("cuda" if use_cuda else "cpu")
    kwargs = {'num_workers': 8, 'pin_memory': True} if use_cuda else {}

    train_dataset = dataset(options.train_list,type=options.type,tile_index =options.index,norm_type=options.norm,norm_range=options.range)
    train_loader = DataLoader(train_dataset, batch_size=1, shuffle=True, **kwargs)

    val_dataset = dataset(options.valid_list,type=options.type,tile_index =options.index,norm_type=options.norm,norm_range=options.range)
    val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False, **kwargs)


    open_doc(options)
    loadUnet = LoadUnet(options,device)
    model,optimizer = loadUnet.Load()
    print('start epoch is {}'.format(options.start_epoch))
    


    print('run!')
    for epoch in range(options.start_epoch, options.epochs+1):
        print(epoch)
        train_loss = train(model, train_loader, optimizer, device, epoch)
        valid_loss = valid(model, val_loader, device)
        write_doc(options,train_loss,valid_loss)
        save_model(model, optimizer, options.model_prefix + 'epoch_{}'.format(epoch))


def main():
    options    = get_train_option()

    print('We need to show the parse options')
    print('******************************************')
    print(options)
    print('******************************************\n')
    train_model(options)


if __name__ == '__main__':
    main()
