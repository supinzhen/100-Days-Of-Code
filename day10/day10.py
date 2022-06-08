import cv2
import numpy as np

img = cv2.imread('D:/joker xue/4.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_ne = img.copy()

img_ne[:,:,0] = 255 - img[:,:,0]
img_ne[:,:,1] = 255 - img[:,:,1]
img_ne[:,:,2] = 255 - img[:,:,2]

cv2.imshow('img',img)
cv2.imshow('negative',img_ne)
cv2.waitKey(0)