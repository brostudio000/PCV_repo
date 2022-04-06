# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 08:47:19 2022

@author: Bro
"""

import cv2 as cv
import numpy as np

img = cv.imread('flower.png')
img2 = cv.imread('its.png')

width = 800
height = 450
size = (width, height)
resize_img2 = cv.resize(img2, size, interpolation=cv.INTER_LINEAR)

hsv = np.double(cv.cvtColor(img, cv.COLOR_BGR2HSV))

lower_bound = np.array([90, 0, 0],dtype="uint8")
upper_bound = np.array([150, 255, 255],dtype="uint8")
mask0 = cv.inRange(hsv, lower_bound, upper_bound)

mask0 = cv.bitwise_not(mask0)
output_img0 = cv.bitwise_and(img,img,mask=mask0)

mask0 = cv.bitwise_not(mask0)
output_img1 = cv.bitwise_and(resize_img2,resize_img2,mask=mask0)

gabung = cv.add(output_img1, output_img0)

#cv.imshow('image', img)
#cv.imshow('image2', resize_img2)
#cv.imshow('mask', mask0)
cv.imshow('gabung1', output_img1)
cv.imshow('gabung', output_img0)
cv.imshow('gabung2', gabung)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()