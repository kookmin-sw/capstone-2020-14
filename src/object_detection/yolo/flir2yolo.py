from __future__ import print_function
import argparse
import glob
import os
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", help='Directory of json files containing annotations')
    parser.add_argument(
        "--output_path", help='Output directory for image.txt files')
    args = parser.parse_args()
    json_files = sorted(glob.glob(os.path.join(args.path, '*.json')))
    file_names = sorted(os.listdir(args.path))

    for json_file, file_name in zip(json_files, file_names):
        print(json_file)
        with open(json_file) as f:
            data = json.load(f)
            annotations = data['annotation']

            width = 640.0
            height = 512.0
            
            converted_results = []

            # {18, 1, 2, 3} -> # [3, 0, 1, 2]
            for ann in annotations:
                if int(ann['category_id']) == 18:
                    cat_id = 3
                else:
                    cat_id = int(ann['category_id']) - 1

                left, top, bbox_width, bbox_height = map(float, ann['bbox'])
                x_center, y_center = (left + bbox_width / 2, top + bbox_height / 2)

                # darknet expects relative values wrt image width&height
                x_rel, y_rel = (x_center / width, y_center / height)
                w_rel, h_rel = (bbox_width / width, bbox_height / height)
                converted_results.append((cat_id, x_rel, y_rel, w_rel, h_rel))
                
            image_name = file_name.split('.')[0]
            file = open(args.output_path + str(image_name) + '.txt', 'w+')
            file.write('\n'.join('%d %.6f %.6f %.6f %.6f' % res for res in converted_results))
            file.close()

