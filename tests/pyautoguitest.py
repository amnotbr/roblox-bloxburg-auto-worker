#!usr/bin/python 
import pyautogui
import cv2
import numpy
import os
import sys

def main():
    s = pyautogui.screenshot()
    s = numpy.array(s)
    
    #show the screen
    
    cv2.imshow("Window", s)
    cv2.waitKey(0)

main()