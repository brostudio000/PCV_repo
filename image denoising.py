# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 06:31:57 2022

@author: Bro
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Import source image
img = cv.imread('C:\\Users\\hp\\Desktop\\part7.png') #Change this path to your source image path

#Denoising function
dst = cv.fastNlMeansDenoisingColored(img,None,6,10,7,21)

#Show the result in 2 different windows
cv.imshow('frame1', img)
cv.imshow('frame2', dst)
ch = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
