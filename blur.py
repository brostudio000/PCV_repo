# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:39:00 2022

@author: Bro
"""

import numpy as np
import cv2

f = cv2.imread('sample2.png')
img=np.copy(f)
f = np.double(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))/255
b,k =f.shape
fa =np.zeros([b,k])

for i in range(1,b-1):
    for j in range(1,k-1):
        fa[i,j]=f[i,j]*1/9+f[i-1,j]*1/9+f[i+1,j]*1/9+f[i,j-1]*1/9+f[i,j+1]*1/9+f[i-1,j-1]*1/9+f[i+1,j+1]*1/9+f[i-1,j+1]*1/9+f[i+1,j-1]*1/9

cv2.imshow('frame', f)
cv2.imshow('frame2', fa)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()