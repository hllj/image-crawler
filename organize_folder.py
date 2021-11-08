import cv2
import argparse
import os
from glob import glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description='Organize image folder with name tag'
                )
    parser.add_argument('--dir', type=str,
                        help='Folder to organize')
    args = parser.parse_args()

    list_file = glob(os.path.join(args.dir, '*'))

    idx = 0
    for file in list_file:
        tag = args.dir
        old_name = file.split('/')[-1]
        new_name = tag + '_' + '%03d' % (idx) + '.jpg'
        idx += 1
        img = cv2.imread(os.path.join(args.dir, old_name))
        cv2.imwrite(os.path.join(args.dir, new_name), img)
        os.remove(os.path.join(args.dir, old_name))
         
