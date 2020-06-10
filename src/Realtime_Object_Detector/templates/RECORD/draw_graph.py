import json # import json module
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
folder_name = 'laboratory'

label_name = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'NONE', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'NONE', 'backpack', 'umbrella', 'NONE', 'NONE', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'NONE', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'NONE', 'dining table', 'NONE', 'NONE', 'toilet', 'NONE', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'NONE', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

bird_dict = {}
with open(folder_name + "/inference.json") as json_file:
    bird_dict = json.load(json_file)


bird_dict["boundingbox"] = sorted(bird_dict["boundingbox"], key = lambda box : box['image_name'])

count_label = []

for box in bird_dict["boundingbox"]:
  # print(box['label'])
    count_label_T = [0 for i in range(90)]
    for label in box['label']:
      count_label_T[int(label)] +=1
    count_label.append(count_label_T)
  # plt.plot([1, 2, 3, 4])
  # plt.show()
  # break 
count_label = np.array(count_label)
object_per_frame = [0 for i in range(90)]
for i in range(90):
  object_per_frame[i] = count_label[:,i:i+1]

is_object = [False for i in range(90)]
i = 500
j = 0
# print(sum(object_per_frame[j][max(0, i-10) :min(i+10, len(object_per_frame[0]))]))
# print(sum(object_per_frame[j][max(0, i-10) :min(i+10, len(object_per_frame[0]))]) > min(i+10, len(object_per_frame[0])) - max(0, i-10) * 0.7)

# exit(True)
for i in tqdm(range(len(object_per_frame[0]))):  
  for j in range(90):
  #    if sum(object_per_frame[j][max(0,i-80): i]) > max(i-80, i) * 0.5:
    if not is_object[j] and  sum(object_per_frame[j]) > 40 and sum(object_per_frame[j][max(0, i-10) :min(i+10, len(object_per_frame[0]))]) > (min(i+10, len(object_per_frame[0])) - max(0, i-10)) * 0.7:
      is_object[j] = True
      print(label_name[j])

for i in tqdm(range(len(object_per_frame[0]))):  
  fig = plt.figure(figsize=(5, 5))
  for j in range(90):
#    if sum(object_per_frame[j][max(0,i-80): i]) > max(i-80, i) * 0.5:
    if is_object[j]:
      if i < 100:
        plt.plot([i for i in range(i)], object_per_frame[j][:i], label=label_name[j])
      else:
        plt.plot([i for i in range(i-100, i)],object_per_frame[j][i-100:i], label=label_name[j])
  plt.legend()
  plt.savefig(folder_name + '/graph/' + str(i).zfill(5) + '.png')
  plt.close(fig)



fig = plt.figure(figsize=(5, 5))
for j in range(90):
  if sum(object_per_frame[j]) > 50:
    plt.plot(object_per_frame[j][:], label=label_name[j])

plt.legend()
plt.savefig(folder_name + '/Total_graph.png')
plt.close(fig)

# import matplotlib.pyplot as plt
# plt.plot([0,1,2,3,4], [0,2,4,6,8])
# plt.show()