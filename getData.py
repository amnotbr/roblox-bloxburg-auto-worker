"""
Module Name: getData.py
Description: Getting the data through screenshots
            Hit the letter u to take a screenshot, idea is to parse screenshots later

Author: amnotbr
Data: 2025-05-26

EDIT: I complete fucking forgot to svae the coordinates maybe that would fucking make all the data easier to work with or something lmao

"""

#!/usr/bin/env python3

import cv2
import keyboard
import numpy
import dxcam
import pyautogui
from PIL import Image
import time
import os

def screenshot(x,y,width,height):
    # create the dx camera

    frame = camera.grab(region=convert_XYWH_to_LTRB(x,y,width,height))  # get the image from the region
    frame = numpy.array(frame, dtype="uint8")
   
    return frame



def store_data(x,y,width,height):
    data = (x,y,width,height)
    
    with open("saveData.txt", "w")as f: 
        for a in data:
            f.write(f"{a}\n")
    

def convert_XYWH_to_LTRB(x: int,y: int,w: int,h: int) -> tuple[int,int,int,int]:
    left = x
    top = y
    right = x + w
    bottom = y + h
    return (left, top, right, bottom)


def region_calc():
    # if there is nothing in the file
    if os.path.getsize("saveData.txt") == 0:
        print("SAVED COORDINATES DO NOT EXIST PLEASE MAKE A BOX AROUND AREA")
        input("click: ")
        x,y = pyautogui.position()
    
        input("next click: ")
        sx,sy = pyautogui.position()
    
    
        width = (sx-x)
        height = (sy-y)
    
        store_data(x,y,width,height)
        return x, y, width, height
    
    # other wise just return whatever is found in the file
    else:
        print("SAVE COORDINATES EXIST")
        with open("saveData.txt", "r") as f:
            x = int(f.readline().strip())
            y = int(f.readline().strip())
            width = int(f.readline().strip())
            height = int(f.readline().strip())



            print(x,y,width,height)
            return x,y,width,height


#  this is to check if there is any data within the file that stores the last saved_image
def open_lastSaved():
    if os.path.getsize("last_saved.txt"):
        num = int(last_saved.read())
    else:
        num = 0

    return num


def main():
    # setup the camera class
    global camera
    camera = dxcam.create()
    count = 0
    
    # setup the loop variable
    num = open_lastSaved()
    run = True
    count = num
    
    # before anything happend we need to find the area in which to take screenshots
    x,y,width,height = region_calc()
    print(f"Starting at number: {count}")


    while count < 926:
        # setup the keyboard to take a screenshot

        if keyboard.is_pressed("u"):
            frame = screenshot(x,y,width,height)
            filename = f"./assets/{count}.png"
            
            cv2.imwrite(filename, frame)
            print(f"Screenshot saved as {filename}\n count: {count}")
            
            count += 1
            time.sleep(2)
            
        elif keyboard.is_pressed("i"):
            with open("last_saved.txt", "w")as f:
                f.write(str(count))
            break

      
        with open("last_saved.txt", "w")as f:
            f.write(str(count))
        
main()
