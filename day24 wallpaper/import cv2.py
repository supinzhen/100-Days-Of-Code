import cv2
import numpy as np

img = cv2.imread('actgo-l3mtz.jpg')
#img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_copy = img.copy()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j,:] = 255 - img_copy[i,j,:]

cv2.imshow('img',img_copy)
cv2.imshow('result',img)
cv2.imwrite('0626.jpg',img)
cv2.waitKey(0)