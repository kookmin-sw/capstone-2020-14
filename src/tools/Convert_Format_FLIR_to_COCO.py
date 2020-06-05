import json
import os
FLIR_path = "FLIR/validation/Annotations/"
file = os.listdir(FLIR_path)


FLIR_dict = []
write_dict = {}


for f in file:
    with open(FLIR_path + f) as json_data:
        dict = json.load(json_data)
        FLIR_dict.append(dict)



write_dict["info"] = {}
write_dict["info"]["description"] = "FLIR DATASET"
write_dict["info"]["url"] = "https://www.flir.com/oem/adas/adas-dataset-form/"
write_dict["info"]["version"] = "1.0"
write_dict["info"]["year"] = 2020
write_dict["info"]["contributor"] = "FLIR"
write_dict["info"]["date_created"] = "2020/05/14"


write_dict["licenses"] = []
write_dict["licenses"].append({
    "url" : "https://www.flir.com/oem/adas/adas-dataset-form/",
    "id" : 1,
    "name" : "FLIR"
}
)

from copy import deepcopy
write_dict["images"] = []
write_dict["annotations"] = []
for i, data in enumerate(FLIR_dict):
    images = {}
    images["license"] = 1
    images["file_name"] = data["image"]["file_name"] + ".jpeg"
    images["FLIR_url"] = "https://www.flir.com/oem/adas/adas-dataset-form/"
    images["height"] = data["image"]["height"]
    images["width"] = data["image"]["width"]
    images["date_captured"] = "don't know"
    images["flickr_url"] = "don't know"
    images["id"] = data["image"]["id"]
    
    for annotation in data["annotation"]:
        annotations = {}
        annotations["segmentation"] = [list(map(float,annotation["segmentation"][0]))]
        annotations["area"] = float(annotation["area"])
        annotations["iscrowd"] = annotation["iscrowd"]
        annotations["image_id"] = annotation["image_id"]
        annotations["bbox"] = list(map(float,annotation["bbox"]))
        annotations["category_id"] = int(annotation["category_id"])
        annotations["id"] = annotation["id"]
        write_dict["images"].append(deepcopy(images))
        write_dict["annotations"].append(deepcopy(annotations))

write_dict["categories"] = []

with open("FLIR/validation/catids.json") as categories:
    write_dict["categories"] = json.load(categories)


with open("instances_val2017.json", "w") as json_data:
    json.dump(write_dict, json_data, indent = 4)
