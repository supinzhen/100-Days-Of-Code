import cv2
import numpy as np

lower = np.array([30,40,300])
upper = np.array([90,100,255])

def empty(v):
    pass

cv2.namedWindow('Mask Adjust')
cv2.createTrackbar('r1','Mask Adjust',0,255,empty)
cv2.createTrackbar('g1','Mask Adjust',0,255,empty)
cv2.createTrackbar('b1','Mask Adjust',0,255,empty)
cv2.createTrackbar('r2','Mask Adjust',255,255,empty)
cv2.createTrackbar('g2','Mask Adjust',255,255,empty)
cv2.createTrackbar('b2','Mask Adjust',255,255,empty)

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if ret:
        r1 = cv2.getTrackbarPos('r1','Mask Adjust')
        g1 = cv2.getTrackbarPos('g1','Mask Adjust')
        b1 = cv2.getTrackbarPos('b1','Mask Adjust')
        r2 = cv2.getTrackbarPos('r2','Mask Adjust')
        g2 = cv2.getTrackbarPos('g2','Mask Adjust')
        b2 = cv2.getTrackbarPos('b2','Mask Adjust')
        lower = np.array([b1,g1,r1])
        upper = np.array([b2,g2,r2])
        mask = cv2.inRange(frame,lower,upper)
        output = cv2.bitwise_and(frame,frame,mask=mask)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        output = cv2.dilate(output,kernel)
        output = cv2.erode(output,kernel)
        cv2.imshow('ori_video',frame)
        cv2.imshow('video',output)
    else:
        break
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        print(b1,g1,r1,b2,g2,r2)
        break