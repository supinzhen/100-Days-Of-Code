import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if ret:
        canny = cv2.Canny(frame,50,100)
        cv2.imshow('video',frame)
        cv2.imshow('canny',canny)

    else:
        break
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break