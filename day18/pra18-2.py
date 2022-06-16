import cv2
import numpy as np

img1 = cv2.imread('D:/joker xue/9.jpg')
img2 = cv2.imread('D:/joker xue/9-1.jpg')
img1 = cv2.resize(img1,(0,0),fx=0.6,fy=0.6)
img2 = cv2.resize(img2,(0,0),fx=0.6,fy=0.6)

img = np.zeros((img1.shape[0],img1.shape[1],3),np.uint8)

def empty(v):
    pass

cv2.namedWindow('adjust')
cv2.createTrackbar('opacity','adjust',50,100,empty)

while True:
    o = cv2.getTrackbarPos('opacity','adjust')
    img[:,:,0] = img1[:,:,0] * ((100-o)/100) + img2[:,:,0] * (o/100)
    img[:,:,1] = img1[:,:,1] * ((100-o)/100) + img2[:,:,1] * (o/100)
    img[:,:,2] = img1[:,:,2] * ((100-o)/100) + img2[:,:,2] * (o/100)

    cv2.imshow('img',img)
    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break