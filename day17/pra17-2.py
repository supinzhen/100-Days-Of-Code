import cv2
import numpy as np

img = np.zeros((400,400,3),np.uint8)

def empty(v):
    pass 

cv2.namedWindow('adjust')
cv2.createTrackbar('radius','adjust',200,400,empty)
cv2.createTrackbar('r','adjust',255,255,empty)
cv2.createTrackbar('g','adjust',255,255,empty)
cv2.createTrackbar('b','adjust',255,255,empty)
cv2.createTrackbar('h','adjust',200,400,empty)
cv2.createTrackbar('w','adjust',200,400,empty)

while True:
    h = cv2.getTrackbarPos('h','adjust')
    w = cv2.getTrackbarPos('w','adjust')
    r = cv2.getTrackbarPos('r','adjust')
    g = cv2.getTrackbarPos('g','adjust')
    b = cv2.getTrackbarPos('b','adjust')
    radius = cv2.getTrackbarPos('radius','adjust')

    img = np.zeros((400,400,3),np.uint8)
    for i in range (400):
        for j in range(400):
            img[i,j,0] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(radius*(2**0.5))*b
            img[i,j,1] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(radius*(2**0.5))*g
            img[i,j,2] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(radius*(2**0.5))*r
            
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break