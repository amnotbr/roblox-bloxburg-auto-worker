"""

"""

import cv2
import sys
import os
import modules.load_img as lim
import dxcam
import keyboard

def _img():
    _obj = lim.LoadImage()
    di = []
    for a in range(0, 35):
        _img_path = f"{a}.png"
        img = _obj.load_image(_img_path)
        if img is not None:
            di.append(img)
    return di

def capture(img):
    pass

def main():
    # step one is to load all the images
    images = _img()
    index = 0
    
    while 1:
        if index >= len(images):
            print("No more images")
            break
        
        cv2.imshow("window", images[index])
        key = cv2.waitKey(0)
        
        index += 1
        

if __name__ == "__main__":
    main()