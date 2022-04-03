import os
import json


json_dir = 'annotations/annotations.json'  # json File path 
out_dir = 'output/'  #  Output  txt  File path 


def main():
    #  Read  json  File data 
    with open(json_dir, 'r') as load_f:
        content = json.load(load_f)
    #  Loop processing 
    for t in content['images']:
        print(t)
        tmp = t['file_name'].split('.')
        filename = out_dir + tmp[0] + '.txt'
        id=t['id']
        for pt in content['annotations']:
          if(pt['image_id']==id):

            if os.path.exists(filename):
                #  Calculation  yolo  The center point required for the data format   relative  x, y  coordinate , w,h  Value 
                x = (pt['bbox'][0] + pt['bbox'][2]/2) / t['width']
                y = (pt['bbox'][1] + pt['bbox'][3]/2) / t['height']
                w = (pt['bbox'][2]) / t['width']
                h = (pt['bbox'][3]) / t['height']
                fp = open(filename, mode="r+", encoding="utf-8")
                file_str = str(pt['category_id']+1) + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
                          ' ' + str(round(h, 6))
                line_data = fp.readlines()

                if len(line_data) != 0:
                    fp.write('\n' + file_str)
                else:
                    fp.write(file_str)
                fp.close()

            #  Create file if it does not exist 
            else:
                fp = open(filename, mode="w", encoding="utf-8")
                fp.close()
                #  Calculation  yolo  The center point required for the data format   relative  x, y  coordinate , w,h  Value 
                x = (pt['bbox'][0] + pt['bbox'][2]/2) / t['width']
                y = (pt['bbox'][1] + pt['bbox'][3]/2) / t['height']
                w = (pt['bbox'][2]) / t['width']
                h = (pt['bbox'][3]) / t['height']
                fp = open(filename, mode="r+", encoding="utf-8")
                file_str = str(pt['category_id']+1) + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
                          ' ' + str(round(h, 6))
                line_data = fp.readlines()

                if len(line_data) != 0:
                    fp.write('\n' + file_str)
                else:
                    fp.write(file_str)
                fp.close()

if __name__ == '__main__':
    main()