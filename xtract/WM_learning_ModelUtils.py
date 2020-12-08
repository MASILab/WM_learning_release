import torch
from torch.nn.functional import interpolate
import numpy as np
from tqdm import tqdm
import nibabel as nib
import os
import re



def load_whichModel(prefix,path='../model'):
    all_file = os.listdir(path)

    min_num = 0
    best_file = ''

    for file in all_file:
        if file.startswith('High_'+prefix):
            last_num = int(file.split('_')[-1])
            if (last_num > min_num):
                best_file = file
                min_num = last_num
    return os.path.join(path,best_file), min_num


def save_nifti(x, save_path, nifti_path):
    nib_img = nib.Nifti1Image(x, nib.load(nifti_path).affine, nib.load(nifti_path).header)
    nib.save(nib_img, save_path)

def train(model, loader, optimizer, device, epoch):
    model.train()
    total_loss = 0
    with tqdm(total=len(loader)) as pbar:
        for batch_idx, sample in enumerate(loader):
            t1 = sample['t1']
            labels = sample['labels']

            t1, labels = t1.to(device), labels.to(device)

            optimizer.zero_grad()

            output = model(t1)

            loss_fun = torch.nn.BCEWithLogitsLoss()
            loss = 0


            for b in range(labels.shape[0]):
                for c in range(labels.shape[1]):
                    if labels[b,c,0,0,0] != -1:
                        loss += loss_fun(output[b,c,:,:,:], labels[b,c,:,:,:])


            total_loss += loss.item()
            loss.backward()
            optimizer.step()
            pbar.set_description("Epoch {}\tAvg Loss: {:.4f}".format(epoch, total_loss/(batch_idx+1)))
            pbar.update(1)

    return total_loss/len(loader)

def valid(model, loader, device):
    model.eval()
    total_loss = 0

    with torch.no_grad():
        with tqdm(total=len(loader)) as pbar:
            for batch_idx, sample in enumerate(loader):
                t1 = sample['t1']
                labels = sample['labels']
                t1, labels = t1.to(device), labels.to(device)

                output = model(t1)
                loss_fun = torch.nn.BCEWithLogitsLoss()
                loss = 0

                for b in range(labels.shape[0]):
                    for c in range(labels.shape[1]):
                        if labels[b,c,0,0,0] != -1:
                            loss += loss_fun(output[b,c,:,:,:], labels[b,c,:,:,:])


                total_loss += loss.item()

                pbar.set_description("Test\tAvg Loss: {:.4f}".format(total_loss/(batch_idx+1)))
                pbar.update(1)

    return total_loss/len(loader)

def save_model(model, optimizer, path):
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict()
    }, path)

def load_checkpoint(model, optimizer, path, device='cuda'):
    checkpoint = torch.load(path,map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    return model, optimizer

def load_model(model, path):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])

    return model

if __name__ == '__main__':
    print(load_whichModel(path,'133'))
