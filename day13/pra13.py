import cv2
from cv2 import threshold
import numpy as np

img = np.zeros((300,300,3),np.uint8)
green = np.zeros((300,300,3),np.uint8)

cv2.circle(img,(100,150),70,(0,127,127),cv2.FILLED)
cv2.circle(green,(170,150),70,(127,0,127),cv2.FILLED)

img_and = cv2.bitwise_and(img,green)
img_and = cv2.cvtColor(img_and,cv2.COLOR_BGR2GRAY)

ret, mask1  = cv2.threshold(img_and, 20, 255, cv2.THRESH_BINARY_INV)

red = np.zeros((300,300,3),np.uint8)

red[:,:,2] = 255
mask_red = cv2.bitwise_xor(img,red,mask = mask1)

cv2.imshow('img',img)
cv2.imshow('green',mask_red)


cv2.waitKey(0)