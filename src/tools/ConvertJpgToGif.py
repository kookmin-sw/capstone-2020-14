


import os
os.system('convert -delay 15 -loop 0  ./pngs/*.png ./UI.gif')
from PIL import Image
import cv2
from tqdm import tqdm
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--ImagePath', type=str,
                    help='TestImageDir', required = True)
parser.add_argument('--GifName', type=str,
                    help='GifName', required = True)
args = parser.parse_args()

Image_dir = args.ImagePath
GifName = args.GifName




result = []
paths = os.listdir(Image_dir)
paths.sort()



# Image_dir = "../Results/Video/Sample/"

# paths = paths[4:200]
# print(paths)
for idx , path in tqdm(enumerate(paths)):
    img = cv2.imread(Image_dir + path)
#    img = cv2.resize(img , (480, 640) , interpolation = cv2.INTER_AREA)
    result.append(img)
    name = path.split(".")[0]
    cv2.imwrite(f'pngs/{name}.png' , img)

print("Generating Image in pngs")


import matplotlib.pyplot as plt
import numpy as np
import imageio
from PIL import Image
import matplotlib.image as mpimg
path = [f"./pngs/{i}" for i in os.listdir("./pngs")]
path.sort()
paths = [ Image.open(i) for i in path]
imageio.mimsave(GifName + '.gif', paths, fps=10)
