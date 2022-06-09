import cv2
import numpy as np

img = cv2.imread('D:/joker xue/4.jpg')
#img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

img_blur = cv2.blur(img,(11,11))
# ksize 指定區域單位
img_gaussianblur = cv2.GaussianBlur(img,(11,11),0)
# ksize 指定區域單位 ( 必須是大於 1 的奇數 )
# sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
img_median = cv2.medianBlur(img,11) 
# ksize 模糊程度 ( 必須是大於 1 的奇數 )

cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gaussian blur',img_gaussianblur)
cv2.imshow('img_median',img_median)
cv2.waitKey(0)