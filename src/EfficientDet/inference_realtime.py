# + endofcell="--"
import cv2
import json
import numpy as np
import os
import time
import glob

from model import efficientdet
from utils import preprocess_image, postprocess_boxes
from utils.draw_boxes import draw_boxes
import argparse
from tqdm import tqdm
import copy
import numpy as np
import cv2
from mss import mss
from PIL import Image


# # +
def main():
    parser = argparse.ArgumentParser()
    
    model_path = parser.add_argument('--model_path', required = True)
    GPU = parser.add_argument('--GPU', default = '0')
#    image_path = parser.add_argument('--image_path', required = True)
    save_path = parser.add_argument('--save_path', required = True)
    json_path = parser.add_argument('--json_path', default = 'default_path_json.json')
    image_size = parser.add_argument('--image_size')
#    file_format = parser.add_argument('--file_format', default = 'jpeg')
    score_threshold = parser.add_argument('--score_threshold', default = 0.3)
    phi = parser.add_argument('--phi', default = 0, type = int)
    args = parser.parse_args()

    json_dict = {}
    json_dict["boundingbox"] = []

    os.environ['CUDA_VISIBLE_DEVICES'] = args.GPU
    # print(args.image_path + '/*.' + args.file_format)
    # file_lists = glob.glob(args.image_path + '/*.' + args.file_format)
    # length = len(file_lists)
    iteration = 0
    # print(length)

    
    print(args)
    
    weighted_bifpn = True
    model_path = args.model_path
    image_sizes = (512, 640, 768, 896, 1024, 1280, 1408)
    image_size = image_sizes[args.phi]
    # coco classes
    classes = {value['id'] - 1: value['name'] for value in json.load(open('coco_90.json', 'r')).values()}
    num_classes = 90
    score_threshold = 0.3
    colors = [np.random.randint(0, 256, 3).tolist() for _ in range(num_classes)]
    _, model = efficientdet(phi=args.phi,
                            weighted_bifpn=weighted_bifpn,
                            num_classes=num_classes,
                            score_threshold=score_threshold)
    
    model.load_weights(model_path, by_name=True)
    print(model_path)
    try:
        os.makedirs(args.save_path)
    except:
        print(args.save_path, "is aleardy exist")
        pass
    start = time.time()
    mon = {'top': 87, 'left': 224, 'width': 590, 'height': 950} # full screen

    # mon = {'top': 297, 'left': 224, 'width': 590, 'height': 450}
    sct = mss()
    while 1:
        sct.get_pixels(mon)
        image = np.array(Image.frombytes('RGB', (sct.width, sct.height), sct.image))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        src_image = image.copy()




        image = image[:, :, :]
        h, w = image.shape[:2]

        image, scale = preprocess_image(image, image_size=image_size)
        # run network
        boxes, scores, labels = model.predict_on_batch([np.expand_dims(image, axis=0)])
        boxes, scores, labels = np.squeeze(boxes), np.squeeze(scores), np.squeeze(labels)
        
        boxes = postprocess_boxes(boxes=boxes, scale=scale, height=h, width=w)

        # select indices which have a score above the threshold
        indices = np.where(scores[:] > score_threshold)[0]

        # select those detections
        boxes = boxes[indices]
        labels = labels[indices]
        # file_name = image_path.split('/')[-1]
        # cv2.imwrite(args.save_path +'/' + file_name, src_image)

        temp_dict = {}
        temp_dict["box"] = boxes[indices].tolist()
        temp_dict["label"] = labels[indices].tolist()
        temp_dict["label_name"] = [classes[int(i)] for i in labels]
        # temp_dict["image_name"] = file_name
        json_dict["boundingbox"].append(copy.deepcopy(temp_dict))

        draw_boxes(src_image, boxes, scores, labels, colors, classes)


        cv2.imshow('test', src_image)

    
    print("time : ", time.time()-start)
    with open(args.json_path ,'w') as json_data:
        json.dump(json_dict, json_data, indent = 4)
# -

if __name__ == '__main__':
    main()

# python inference_realtime.py --GPU 0,1 --model_path efficientdet-d0.h5 --save_path Test/ --score_threshold 0.3 --phi 0 --json_path dd.json

# --
