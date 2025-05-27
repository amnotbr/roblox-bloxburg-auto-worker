"""
    This section si soley going to be for getting data n shit
"""

import pyautogui
import numpy
import cv2



def region_calc():
    input("click: ")
    x,y = pyautogui.position()
    
    input("next click: ")
    sx,sy = pyautogui.position()
    
    width = (sx-x)
    height = (sy-y)
    
    #print(x, y, width, height))
    return x, y, width, height

def main():
    x, y, width, height = region_calc()
    
    screen = pyautogui.screenshot(region=(x, y, width, height))
    screen = numpy.array(screen)
    
    cv2.imshow("Window", screen)
    cv2.waitKey(0)

main()