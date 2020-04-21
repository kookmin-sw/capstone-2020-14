# +



import os
os.system('convert -delay 15 -loop 0  ./pngs/*.png ./UI.gif')
from PIL import Image
import cv2
from tqdm import tqdm
result = []
Image_dir = "../Results/Video/Sample/"
paths = os.listdir(Image_dir)
paths.sort()
paths = paths[4:200]
print(paths)
for idx , path in tqdm(enumerate(paths)):
    img = cv2.imread(Image_dir + path)
    img = cv2.resize(img , (320, 240) , interpolation = cv2.INTER_AREA)
    result.append(img)
    name = path.split(".")[0]
    cv2.imwrite(f'pngs/{name}.png' , img)    
# -


import matplotlib.pyplot as plt
import numpy as np
import imageio
from PIL import Image
import matplotlib.image as mpimg
path = [f"./pngs/{i}" for i in os.listdir("./pngs")]
paths = [ Image.open(i) for i in path]
imageio.mimsave('./example_class.gif', paths, fps=10)


