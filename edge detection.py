# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:56:05 2022

@author: Bro
"""

import numpy as np
import cv2
import time

def Conv2(f,kn):
    [nb,nc]=f.shape

    fa=np.zeros([nb,nc])
    
    for y in range(1,nb-1):
        for x in range(1,nc-1):
            for yy in range(-1,2):
                for xx in range(-1,2):
                    fa[y,x]=fa[y,x]+f[y+yy,x+xx]*kn[yy+1,xx+1] 
    return np.copy(fa)

A = time.time()
f = cv2.imread('peppers.png')
#img=np.copy(f)
f = np.double(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))/255
# kh =np.array([[0,-1,0],
#               [-1,4,-1],
#               [0,-1,0]])

k =np.array([[0,-1,0],
             [-1,2,0],
             [0,0,0]])

fa = Conv2(f,k)
fa=np.array(fa)

cv2.imshow('frame', f)
cv2.imshow('fa', fa)
B = time.time()
t = (B-A)
print(t)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()