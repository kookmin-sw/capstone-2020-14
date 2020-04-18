# -*- coding: utf-8 -*-
TestImageDir = "DATASET/FLIR/train/PreviewData"
imageNum = 50
imageIdx = [4,5,6,9]
Modeldir = "Model/FasterRCNN/ModelSample/"
ModelEpoch = 20
saveDir = "Results/Images/Sample/"
ZIP = True
batchSize = 2

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import torch.utils.data
import torch.nn as nn
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.transforms import ToTensor
from tqdm import tqdm
import os
import json
import utils

class Dataset(torch.utils.data.Dataset):
    def __init__(self, root, transforms=None):
        self.root = root
        self.transforms = transforms
        self.imgs = list(sorted(os.listdir(os.path.join(root))))
        self.Kimg = []
    def __getitem__(self, idx):
        img_path = os.path.join(self.root,  self.imgs[idx])
        img = Image.open(img_path).convert("RGB")
        target = []
        
        if self.transforms is not None:
            img = self.transforms(img, target)
        return img

    def __len__(self):
        return len(self.imgs)


def get_transform(train):
    transforms = []
    transforms.append(T.ToTensor())
    if train:
        transforms.append(T.RandomHorizontalFlip(0.5))
    return T.Compose(transforms)



def get_instance_segmentation_model(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=False, 
                                                                 box_nms_thresh = 0.35)
    
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    
    return model




dataset_test = Dataset(TestImageDir, None)
indices = torch.randperm(len(dataset_test)).tolist()
dataset_test = torch.utils.data.Subset(dataset_test, indices[-500:])
data_loader_test = torch.utils.data.DataLoader(
    dataset_test, batch_size=2, shuffle=False, num_workers=1,
    collate_fn=utils.collate_fn)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = get_instance_segmentation_model(6)
model.load_state_dict(torch.load(Modeldir + "epoch" + str(ModelEpoch) + ".pth"))


model.to(device)
try:
    os.mkdir(saveDir)
except OSError:
    pass

for j in tqdm(range(imageNum)):
    img = ToTensor()(dataset_test[j])
    model.eval()
    with torch.no_grad():
        prediction = model([img.to(device)])


    plt.figure(figsize = (15,15))
    plt.imshow(img.permute(1, 2, 0))

    color_set = ['w','r','b','y','g','m']  #각 클래스별로 다른 색깔
    The_boxes = (prediction[0]['boxes']).tolist()
    this_labels = (prediction[0]['labels']).tolist()
    
    for i, box in enumerate(The_boxes):
      x_values = [box[0], box[0], box[2], box[2], box[0]]
      y_values = [box[1], box[3], box[3], box[1], box[1]]
      plt.plot(x_values, y_values, linewidth = 3, color = color_set[this_labels[i]])

    plt.savefig(saveDir + 'result'+ str(j)+ '.png', bbox_inches="tight")
    plt.close()



