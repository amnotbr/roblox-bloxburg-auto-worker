"""
Module Name: getData.py
Description: Getting the data through screenshots
            Hit the letter u to take a screenshot, idea is to parse screenshots later

Author: amnotbr
Data: 2025-05-26
"""

#!/usr/bin/env python3

import cv2
import keyboard
import os
import numpy
import dxcam
import pyautogui
from PIL import Image
import time
import imagehash
import threading

def delete_duplicate(folder_path = "./assets/"):
    pass

def check_for_duplicates(count, folder_path = "./assets/"):
    # idea is to add the file name to the hash, and if one of them are the same, then remove one basically
    store = {}
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if os.path.isfile(file_path):
            img = Image.open(file_path)
            hash_avg = imagehash.average_hash(img)
            print(f"AVERAGE_HASH: {hash_avg}")
            
            store.update({
                f"{count}.png": hash_avg
            })


def screenshot(x,y,width,height):
    # create the dx camera

    frame = camera.grab(region=convert_XYWH_to_LTRB(x,y,width,height))  # get the image from the region
    frame = numpy.array(frame, dtype="uint8")
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    return frame



def store_data(x,y,width,height):
    data = (x,y,width,height)
    
    with open("saveData.txt", "w")as f:
        
        for a in data:
            f.write(f"{a}, ")
    

def convert_XYWH_to_LTRB(x: int,y: int,w: int,h: int) -> tuple[int,int,int,int]:
    left = x
    top = y
    right = x + w
    bottom = y + h
    return (left, top, right, bottom)


def region_calc():
    input("click: ")
    x,y = pyautogui.position()
    
    input("next click: ")
    sx,sy = pyautogui.position()
    
    
    width = (sx-x)
    height = (sy-y)
    
    store_data(x,y,width,height)
    return x, y, width, height


def main():
    # setup the camera class
    global camera
    camera = dxcam.create()

    
    # setup the loop variable
    run = True
    count = 0
    
    # before anything happend we need to find the area in which to take screenshots
    x,y,width,height = region_calc()
    

    while count < 196:
        # setup the keyboard to take a screenshot


        if keyboard.is_pressed("u"):
            frame = screenshot(x,y,width,height)
            filename = f"./assets/{count}.png"
            
            cv2.imwrite(filename, frame)
            print(f"Screenshot saved as {filename}\n count: {count}")
            
            count += 1
            check_for_duplicates()
            time.sleep(2)
            
        elif keyboard.is_pressed("i"):
            break
    
main()