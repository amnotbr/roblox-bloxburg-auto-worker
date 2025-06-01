import cv2
import numpy
import os


class LoadImage:
    def __init__(self):
        self.init_path = "./assets/"

    def load_image(self, image_path):
        new_path = os.path.join(self.init_path, image_path)
        
        img = cv2.imread(new_path)
        
        if img is None:
            print("Error: could not load image ?Possible indirect path")
        
        # convert the color to make sure it is in the correct color format
        if len(img.shape) == 2 or (len(img.shape) == 3 and img.shape[2] == 1):
            color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        else:
            color = img
        
        return color