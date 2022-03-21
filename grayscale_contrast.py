# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:30:56 2022

@author: Bro
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('C:\\Users\\hp\\Desktop\\part7.png')

imgr = np.double (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))/255
b=0.3
alpha=0.6
imcr = (imgr-b)*alpha+b

cv2.imshow('frame1', imgr)
cv2.imshow('frame2', imcr)
ch= cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()