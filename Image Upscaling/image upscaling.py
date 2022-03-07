# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 06:25:54 2022

@author: Bro
"""

import cv2 as cv
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()

#Source image path
img = cv.imread('E:\\Documents\\COLLEGE\\PCV\\sample2.png')

#Upscaling Model path
path = "E:\\Documents\\COLLEGE\\PCV\\LapSRN_x4.pb"
sr.readModel(path)
sr.setModel("lapsrn", 4)

#Upscale operation
result = sr.upsample(img)

#Save result as new image
cv.imwrite("E:\\Documents\\COLLEGE\\PCV\sample2_upscaled_lapsrnx4.png", result)
