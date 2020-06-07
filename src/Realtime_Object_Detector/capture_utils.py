__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from mss import mss
from PIL import Image

import numpy as np
import io
import cv2





import os
import time
import glob
import json
from model import efficientdet
from utils import preprocess_image, postprocess_boxes
from utils.draw_boxes import draw_boxes
import argparse
from tqdm import tqdm
import copy




# TODO => 비디오 화면에 맞춰서 수정할 것.
mon = {'top': 297, 'left': 224, 'width': 590, 'height': 450}


def capture():

    save_path = "RealTimeTest/"
    GPU = '0'
    Model_path = 'efficientdet-d0.h5'
    phi = 0



    json_dict = {}
    json_dict["boundingbox"] = []

    os.environ['CUDA_VISIBLE_DEVICES'] = GPU

    weighted_bifpn = True
    model_path = Model_path
    image_sizes = (512, 640, 768, 896, 1024, 1280, 1408)
    image_size = image_sizes[phi]
    # coco classes
    classes = {value['id'] - 1: value['name'] for value in json.load(open('coco_90.json', 'r')).values()}
    num_classes = 90
    score_threshold = 0.3
    colors = [np.random.randint(0, 256, 3).tolist() for _ in range(num_classes)]
    _, model = efficientdet(phi=phi,
                            weighted_bifpn=weighted_bifpn,
                            num_classes=num_classes,
                            score_threshold=score_threshold)
    
    model.load_weights(model_path, by_name=True)
    try:
        os.makedirs(save_path)
    except:
        print(save_path, "is aleardy exist")
        pass

    start = time.time()
    mon = {'top': 297, 'left': 224, 'width': 590, 'height': 450}
    sct = mss()
    image_num = 0




    while True:
        with mss() as sct:
            sct.get_pixels(mon)
            image = np.array(Image.frombuffer('RGB', (sct.width, sct.height), sct.image))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # # TODO: np_img 에다가 prediction 추가할 것.
            src_image = image.copy()
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




#             if cv2.waitKey(25) & 0xFF == ord('q'):
# #                cv2.destroyAllWindows()
#                 break

            np_img = np.array(src_image)
            encode_return_code, image_buffer = cv2.imencode('.jpg', np_img)
            io_buf = io.BytesIO(image_buffer)
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + io_buf.read() + b'\r\n')
