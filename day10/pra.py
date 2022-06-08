import cv2
import numpy as np

img = cv2.imread('D:/joker xue/11.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_copy = img.copy()

def empty(v):
    pass

cv2.namedWindow('Adjust')
cv2.createTrackbar('R','Adjust',255,400,empty)
cv2.createTrackbar('G','Adjust',255,400,empty)
cv2.createTrackbar('B','Adjust',255,400,empty)

while True:
    img = img_copy.copy()
    r = cv2.getTrackbarPos('R','Adjust') 
    g = cv2.getTrackbarPos('G','Adjust') 
    b = cv2.getTrackbarPos('B','Adjust') 
    img[:,:,0] = (b / 255.0) * img[:, :, 0]
    img[:, :, 0][img[:, :, 0] > 255] = 255
    img[:,:,1] = ( g / 255.0) * img[:, :, 1] 
    img[:, :, 1][img[:, :, 1] > 255] = 255
    img[:,:,2] = ( r / 255.0) * img[:, :, 2]
    img[:, :, 2][img[:, :, 2] > 255] = 255
    cv2.imshow('img',img)
    cv2.imshow('ori',img_copy)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break