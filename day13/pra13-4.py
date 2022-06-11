import cv2
import numpy as np

cap = cv2.VideoCapture('D:/joker xue/C0003.MP4')
white = np.zeros((1080,1920,3),np.uint8)

white[:,:,1] = 255

white_copy = white.copy()
img = cv2.imread('./img.jpg')

lower = np.array([140,175,15])
upper = np.array([255,255,161])

while True:
    ret,frame = cap.read()
    if ret:
        white = white_copy.copy()
        mask1 = cv2.inRange(frame,lower,upper)
        mask2 = cv2.bitwise_not(mask1)
        output = cv2.bitwise_and(frame,frame,mask=mask2)
        white = cv2.bitwise_and(white,white,mask=mask1)
        key = cv2.add(output,white)
        cv2.imshow('video',key)

    else:
        break
    if cv2.waitKey(30) == ord('q'):
        cv2.destroyAllWindows()
        break