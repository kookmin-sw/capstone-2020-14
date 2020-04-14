from tqdm import tqdm

import os

training_image_paths = os.listdir('/root/Desktop/workspace/yolo/FLIR/train/PreviewData/')
validation_image_paths = os.listdir('/root/Desktop/workspace/yolo/FLIR/validation/PreviewData/')

target_path = '/root/Desktop/workspace/yolo/darknet/flir/'

with open('./flir_train.txt', 'w') as f:
    
    result = ''
    
    for file_name in tqdm(training_image_paths):
        path = target_path + file_name + '\n'
        result += path
        
    f.write(result)
    f.close()

with open('./flir_valid.txt', 'w') as f:
    
    result = ''
    
    for file_name in tqdm(validation_image_paths):
        path = target_path + file_name + '\n'
        result += path
        
    f.write(result)
    f.close()

