"""
    Put all basic match template functions in a file
"""

import cv2

def find_image(img, template):
    res = cv2.matchTemplate(img, template, 'TM_COEFF')
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    return max_val, max_loc