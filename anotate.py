#!/usr/bin/python
import os, sys
import numpy
sys.path.pop(2)
import cv2
import time
from os import listdir
clicked = False
buttonDown_x = 0
buttonDown_y = 0
buttonUp_x = 0
buttonUp_y = 0
lineData = ""
counter = 0
path = "/home/vysakh/truck/"
currentPath = ""
files = [f for f in sorted(os.listdir(path))]

def onMouse(event,x,y,flags,para):
    global clicked
    global buttonDown_x
    global buttonDown_y
    global buttonUp_x
    global buttonUp_y
    if event:
        print("*********")

    if event == cv2.EVENT_LBUTTONDOWN:
        buttonDown_x = x
        buttonDown_y = y
    if event == cv2.EVENT_LBUTTONUP:
        buttonUp_x = x
        buttonUp_y = y
        clicked = True
        print((buttonDown_x,buttonDown_y),(buttonUp_x,buttonUp_y))
        global counter
        global currentPath
        counter += 1

        with open("/home/vysakh/truck/"+str(counter).zfill(4)+".txt","w") as dataFile:
            dataFile.write(",".join([currentPath,str(buttonDown_x),str(buttonDown_y),str(buttonUp_x),str(buttonUp_y),"truck"]))

def mark_image(data_path):
    global clicked
    cv2.namedWindow(data_path)
    cv2.setMouseCallback(data_path,onMouse)
    image = cv2.imread(data_path)
    print("image path: ",data_path)
    cv2.imshow(data_path,image)
    cv2.waitKey(0)
    cv2.destroyWindow(data_path)

def getNextImage():
    global files
    global path
    if len(files)==0:
        return None
    current = files.pop(0)
    print path+current
    return path+current

if __name__ == "__main__":
    while True:
        current = getNextImage()
        if current!=None:
            global currentPath
            currentPath = current
            mark_image(current)
        else:
            print("finish")
            break
