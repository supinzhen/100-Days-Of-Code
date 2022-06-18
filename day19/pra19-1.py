import cv2
import numpy as np

w = 400
h = 400

img = np.zeros((400,400,3),np.uint8)
red = np.zeros((400,400,3),np.uint8)
output = np.zeros((400,400,3),np.uint8)

def color(v):
    pass

cv2.namedWindow('adjust')
cv2.createTrackbar('r1','adjust',255,255,color)
cv2.createTrackbar('g1','adjust',0,255,color)
cv2.createTrackbar('b1','adjust',0,255,color)
cv2.createTrackbar('r2','adjust',0,255,color)
cv2.createTrackbar('g2','adjust',255,255,color)
cv2.createTrackbar('b2','adjust',0,255,color)

while True:
    img = np.zeros((400,400,3),np.uint8)
    red = np.zeros((400,400,3),np.uint8)
    output = np.zeros((400,400,3),np.uint8)
    r1 = cv2.getTrackbarPos('r1','adjust')
    g1 = cv2.getTrackbarPos('g1','adjust')
    b1 = cv2.getTrackbarPos('b1','adjust')
    r2 = cv2.getTrackbarPos('r2','adjust')
    g2 = cv2.getTrackbarPos('g2','adjust')
    b2 = cv2.getTrackbarPos('b2','adjust')
    img[:,:,0] = b1
    img[:,:,1] = g1
    img[:,:,2] = r1

    red[:,:,0] = b2
    red[:,:,1] = g2
    red[:,:,2] = r2

    for i in range (400):
        output[i,:,0] = b1 * i//400 + b2 *(400-i)//400
        output[i,:,1] = g1 * i//400 + g2 *(400-i)//400
        output[i,:,2] = r1 * i//400 + r2 *(400-i)//400

    cv2.imshow('img',img)
    cv2.imshow('red',red)
    cv2.imshow('output',output)

    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('output.png',output)
        cv2.destroyAllWindows()
        break