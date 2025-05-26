import cv2
import numpy
import os

class ImportImage:
    def __init__(self):
        # define the paths of the images and load them through a function
        self.folder_path = "/assets/"
        self.images = []
        self.filenames = []
        
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.folder_path = os.path.join(self.script_dir, '..', 'assets')
    
    def load(self):
        for file in os.listdir(self.folder_path):
            image = cv2.imread(os.path.join(self.folder_path, file))
            
            if image is not None:
                self.images.append(image)
                self.filenames.append(file)
        
        return self.images, self.filenames