import cv2
import numpy as np

img = cv2.imread('D:/joker xue/4.jpg')
img = cv2.resize(img,(0,0),fx=0.6,fy=0.6)
img_copy = img.copy()

def empty(v):
    pass

size = img.shape

cv2.namedWindow('mosaic adjust')
cv2.createTrackbar('level','mosaic adjust',1,20,empty)
cv2.createTrackbar('x1','mosaic adjust',0,size[0],empty)
cv2.createTrackbar('x2','mosaic adjust',size[0],size[0],empty)
cv2.createTrackbar('y1','mosaic adjust',0,size[1],empty)
cv2.createTrackbar('y2','mosaic adjust',size[1],size[1],empty)

level = 1 #縮小比例，可以當作馬賽克的等級
while True:
    img = img_copy.copy()
    level = cv2.getTrackbarPos('level','mosaic adjust')
    x1 = cv2.getTrackbarPos('x1','mosaic adjust')
    x2 = cv2.getTrackbarPos('x2','mosaic adjust')
    y1 = cv2.getTrackbarPos('y1','mosaic adjust')
    y2 = cv2.getTrackbarPos('y2','mosaic adjust')
    if level == 0 :
        level = 1
    h = int((x2-x1)/level)
    w = int((y2-y1)/level)
    mosaic = img[x1:x2,y1:y2]
    mosaic = cv2.resize(mosaic,(w,h),interpolation = cv2.INTER_LINEAR) #根據縮小尺寸縮小
    mosaic = cv2.resize(mosaic,(y2-y1,x2-x1),interpolation = cv2.INTER_NEAREST) #放大到原本大小

    img[x1:x2,y1:y2] = mosaic

    cv2.imshow('img',img)
    cv2.imshow('mosaic',mosaic)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break