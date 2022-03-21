# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:39:02 2022

@author: Bro
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
img = np.double(cv2.imread('C:\\Users\\hp\\Desktop\\part7.png'))/255

b,k,w = img.shape

imbri =np.zeros([b,k,w])
c=-0.15

for i in range(b):
    for j in range(k):
        imbri[i,j,0]=img[i,j,0]+c
        imbri[i,j,1]=img[i,j,1]+c
        imbri[i,j,2]=img[i,j,2]+c
        

cv2.imshow('frame1', img)
cv2.imshow('frame2', imbri)
ch= cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()