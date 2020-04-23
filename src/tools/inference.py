# -*- coding: utf-8 -*-


import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import torch.utils.data
import torch.nn as nn
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.transforms import ToTensor
#from tqdm.notebook import tqdm
from tqdm import tqdm
import os
import json
import utils
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


INF = 999999999
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--TestImageDir', type=str,
                    help='TestImageDir', required = True)
parser.add_argument('--Modeldir', type=str,
                    help='Model directory', required = True)
parser.add_argument('--saveDir', type=str,
                    help='Path to images to be inferred', required = True)
parser.add_argument('--ModelEpoch', type=int, default=20,
                    help='Model epoch', required = True)


parser.add_argument('--MaximageNum', type=int,
                    help='Path to save detection output', default = INF)

parser.add_argument('--ZIP', type=bool, default=True,
                    help='Patch size, width and height of patch is equal.')
parser.add_argument('--batchSize', type=int, default=2,
                    help='Patch size, width and height of patch is equal.')
# parser.add_argument('--imageIdx', type=int, default=2,
#                     help='Patch size, width and height of patch is equal.')
args = parser.parse_args()



TestImageDir = args.TestImageDir
Modeldir = args.Modeldir
saveDir = args.saveDir

MaximageNum = args.MaximageNum
# imageIdx = args.imageIdx
ModelEpoch = args.ModelEpoch
ZIP = args.ZIP
batchSize = args.batchSize

if MaximageNum < 0 or MaximageNum == INF:
    MaxImageNum = len(os.listdir(TestImageDir))



# TestImageDir = "DATASET/FLIR/train/PreviewData"
# Modeldir = "Model/FasterRCNN/ModelSample/"
# saveDir = "Results/Images/Sample/"

# MaximageNum = 50
# imageIdx = [4,5,6,9]
# ModelEpoch = 20
# ZIP = True
# batchSize = 2

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


import torchvision.models.detection as TT
from torchvision.models.detection.backbone_utils import resnet_fpn_backbone
from torchvision.models.detection import FasterRCNN

# def resnet_fpn_backbone(backbone_name, pretrained):
#     backbone = resnet.__dict__[backbone_name](
#         pretrained=pretrained,
#         norm_layer=misc_nn_ops.FrozenBatchNorm2d)
#     # freeze layers
#     for name, parameter in backbone.named_parameters():
#         if 'layer2' not in name and 'layer3' not in name and 'layer4' not in name:
#             parameter.requires_grad_(False)

#     return_layers = {'layer1': 0, 'layer2': 1, 'layer3': 2, 'layer4': 3}

#     in_channels_stage2 = 256
#     in_channels_list = [
#         in_channels_stage2,
#         in_channels_stage2 * 2,
#         in_channels_stage2 * 4,
#         in_channels_stage2 * 8,
#     ]
#     out_channels = 256
#     return BackboneWithFPN(backbone, return_layers, in_channels_list, out_channels)

def fasterrcnn_resnet101_fpn(pretrained=False, progress=False,
                            num_classes=91, pretrained_backbone=True, **kwargs):
    """
    Constructs a Faster R-CNN model with a ResNet-101-FPN backbone.
    The input to the model is expected to be a list of tensors, each of shape ``[C, H, W]``, one for each
    image, and should be in ``0-1`` range. Different images can have different sizes.
    The behavior of the model changes depending if it is in training or evaluation mode.
    During training, the model expects both the input tensors, as well as a targets (list of dictionary),
    containing:
        - boxes (``FloatTensor[N, 4]``): the ground-truth boxes in ``[x1, y1, x2, y2]`` format, with values
          between ``0`` and ``H`` and ``0`` and ``W``
        - labels (``Int64Tensor[N]``): the class label for each ground-truth box
    The model returns a ``Dict[Tensor]`` during training, containing the classification and regression
    losses for both the RPN and the R-CNN.
    During inference, the model requires only the input tensors, and returns the post-processed
    predictions as a ``List[Dict[Tensor]]``, one for each input image. The fields of the ``Dict`` are as
    follows:
        - boxes (``FloatTensor[N, 4]``): the predicted boxes in ``[x1, y1, x2, y2]`` format, with values between
          ``0`` and ``H`` and ``0`` and ``W``
        - labels (``Int64Tensor[N]``): the predicted labels for each image
        - scores (``Tensor[N]``): the scores or each prediction
    Example::
        >>> model = torchvision.models.detection.fasterrcnn_resnet101_fpn(pretrained=False)
        >>> model.eval()
        >>> x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
        >>> predictions = model(x)
    Arguments:
        pretrained (bool): If True, returns a model pre-trained on COCO train2017(currently don't have pre-trained models)
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    if pretrained:
        raise Exception("resnet101 cannot use pre-trained models") 
        # no need to download the backbone if pretrained is set
        pretrained_backbone = False
    backbone = resnet_fpn_backbone('resnet101', pretrained_backbone)
    model = FasterRCNN(backbone, num_classes, **kwargs)
    if pretrained:
        state_dict = load_state_dict_from_url(model_urls['fasterrcnn_resnet101_fpn_coco'],
                                              progress=progress)
        model.load_state_dict(state_dict)
    return model





def get_instance_segmentation_model(num_classes):
    model = fasterrcnn_resnet101_fpn(pretrained=False, box_nms_thresh = 0.35, num_classes = num_classes)
    
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    
    return model




dataset_test = Dataset(TestImageDir, None)
#indices = torch.randperm(len(dataset_test)).tolist()
indices = [i for i in range(len(dataset_test))]
dataset_test = torch.utils.data.Subset(dataset_test, indices[0:-1])
data_loader_test = torch.utils.data.DataLoader(
    dataset_test, batch_size=2, shuffle=False, num_workers=1,
    collate_fn=utils.collate_fn)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = get_instance_segmentation_model(6)
model.load_state_dict(torch.load(Modeldir + "epoch" + str(ModelEpoch) + ".pth"))


# +
model.to(device)
try:
    os.mkdir(saveDir)
except OSError:
    pass

file_list = sorted(os.listdir(TestImageDir))
file_list[:4]
# -

for j in tqdm(range(len(dataset_test))):
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

    plt.savefig(saveDir + 'result_'+ file_list[j], bbox_inches="tight")
    plt.close()



