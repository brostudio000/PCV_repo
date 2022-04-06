# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:45:43 2022

@author: Bro
"""

import cv2 as cv
import numpy as np

cap1 = cv.VideoCapture(1)
img = cv.imread('bg.png')

width = 640
height = 480
size = (width, height)
resize_img2 = cv.resize(img, size, interpolation=cv.INTER_AREA)

while True:
    ret1, frame1 = cap1.read()
    
    hsv = np.double(cv.cvtColor(frame1, cv.COLOR_BGR2HSV))
    
    lower_bound = np.array([90, 0, 0],dtype="uint8")
    upper_bound = np.array([150, 255, 255],dtype="uint8")
    mask0 = cv.inRange(hsv, lower_bound, upper_bound)

    mask0 = cv.bitwise_not(mask0)
    output_img0 = cv.bitwise_and(frame1,frame1,mask=mask0)

    mask0 = cv.bitwise_not(mask0)
    output_img1 = cv.bitwise_and(resize_img2,resize_img2,mask=mask0)
    
    gabung = cv.add(output_img1, output_img0)
    
    cv.imshow('cam1', frame1)
    cv.imshow('gabung', gabung)
    #cv.imshow('gambar', resize_img2)
    
    if cv.waitKey(1) == ord('q'):
        break
cap1.release()
cv.destroyAllWindows()
