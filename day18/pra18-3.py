import cv2
import numpy as np

cap = cv2.VideoCapture(1)

def empty(v):
    pass

cv2.namedWindow('adjust')
cv2.createTrackbar('opacity','adjust',50,100,empty)
cv2.createTrackbar('r','adjust',50,255,empty)
cv2.createTrackbar('g','adjust',50,255,empty)
cv2.createTrackbar('b','adjust',50,255,empty)

while True:
    ret,frame = cap.read()
    o = cv2.getTrackbarPos('opacity','adjust')
    r = cv2.getTrackbarPos('r','adjust')
    g = cv2.getTrackbarPos('g','adjust')
    b = cv2.getTrackbarPos('b','adjust')
    if ret:
        img = np.zeros((frame.shape[0],frame.shape[1],3),np.uint8)
        output = np.zeros((frame.shape[0],frame.shape[1],3),np.uint8)
        img[:,:,0] = b
        img[:,:,1] = g
        img[:,:,2] = r
        output[:,:,:] = img[:,:,:] * (o/100)  + frame[:,:,:] *((100-o)/100)
        cv2.imshow('video',output)

    else:
        break
    if cv2.waitKey(30) == ord('q'):
        cv2.destroyAllWindows()
        break