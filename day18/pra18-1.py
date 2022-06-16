import cv2
import numpy as np

img1 = cv2.imread('D:/joker xue/9.jpg')
img2 = cv2.imread('D:/joker xue/9-1.jpg')
img1 = cv2.resize(img1,(0,0),fx=0.6,fy=0.6)
img2 = cv2.resize(img2,(0,0),fx=0.6,fy=0.6)

img1_copy = img1.copy()
w = img1.shape[1]
h = img2.shape[0]

def empty(v):
    global img1
    radius = cv2.getTrackbarPos('radius','adjust')
    c_h = cv2.getTrackbarPos('h','adjust')
    c_w = cv2.getTrackbarPos('w','adjust')
    o = cv2.getTrackbarPos('opacity','adjust')
    img1 = img1_copy.copy()
    for i in range(w):
        for j in range(h):
            num = int(((j-c_h)*(j-c_h)+(i-c_w)*(i-c_w))**0.5)/(radius*(2**0.5))
            img1[j,i,:] = img1[j,i,:] *(1-num) + img2[j,i,:]*(num)

    img1[:,:,:] = img1[:,:,:] * ((100-o)/100) + img2[:,:,:] * (o/100)

cv2.namedWindow('adjust')
cv2.createTrackbar('h','adjust',img2.shape[0]//2,img2.shape[0],empty)
cv2.createTrackbar('w','adjust',img2.shape[1]//2,img2.shape[1],empty)
cv2.createTrackbar('radius','adjust',img2.shape[0]//2,img2.shape[0],empty)
cv2.createTrackbar('opacity','adjust',50,100,empty)

while True:
    cv2.imshow('img',img1)
    cmd = cv2.waitKey(1)
    if cmd == ord('q'):
        cv2.destroyAllWindows()
        break
    if cmd == ord('w'):
        file_name = 'pra18-1.jpg'
        cv2.imwrite(file_name,img1)
