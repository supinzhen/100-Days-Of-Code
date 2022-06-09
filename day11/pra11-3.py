import cv2
import numpy as np

img = cv2.imread('D:/joker xue/2.jpg')
#img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_copy = img_gray.copy()
ret, output = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# ret ??¯å?¦æ?????è½????ï¼??????? Trueï¼?å¤±æ?? False
# img ä¾?æº?å½±å??
# thresh ??¾å?¼ï?????å¸¸è¨­å®? 127
# maxval ???å¤§ç?°åº¦ï¼????å¸¸è¨­å®? 255
# type è½??????¹å??

def empty(v):
    pass

cv2.namedWindow('Adjust Transhold')
cv2.createTrackbar('Value','Adjust Transhold',127,255,empty)

while True:
    img_gray_copy = img_gray.copy()
    val = cv2.getTrackbarPos('Value','Adjust Transhold')
    img_blur = cv2.medianBlur(img_gray_copy,101)
    output2 = cv2.adaptiveThreshold(img_gray_copy, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
    img_gray_copy[:,:][img_gray_copy[:,:]>val] = 255
    img_gray_copy[:,:][img_gray_copy[:,:]<=val] = 0
    # img ä¾?æº?å½±å??
    # maxValue ???å¤§ç?°åº¦ï¼????å¸¸è¨­å®? 255
    # adaptiveMethod ??ªé?©æ??äº???¼å??è¨?ç®???¹æ??
    # thresholdType äº???¼å??è½??????¹å??
    # blockSize è½??????????å¤§å??ï¼????å¸¸è¨­å®? 11
    # C ???ç§»é??ï¼????å¸¸è¨­å®? 2
    cv2.imshow('img',output2)
    cv2.imshow('img2',img_gray_copy)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break