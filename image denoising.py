# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 06:31:57 2022

@author: Bro
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:\\Users\\hp\\Desktop\\part7.png')

dst = cv.fastNlMeansDenoisingColored(img,None,6,10,7,21)

#plt.subplot(121),plt.imshow(img)
#plt.subplot(122),plt.imshow(dst)
#plt.show()
cv.imshow('frame1', img)
cv.imshow('frame2', dst)
ch = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()