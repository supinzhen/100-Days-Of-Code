import cv2
import numpy as np

img = cv2.imread('D:/joker xue/2.jpg')
#img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_copy = img_gray.copy()
ret, output = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# ret ??��?��?????�????�??????? True�?失�?? False
# img �?�?影�??
# thresh ??��?��?????常設�? 127
# maxval ???大�?�度�????常設�? 255
# type �??????��??

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
    # img �?�?影�??
    # maxValue ???大�?�度�????常設�? 255
    # adaptiveMethod ??��?��??�???��??�?�???��??
    # thresholdType �???��??�??????��??
    # blockSize �??????????大�??�????常設�? 11
    # C ???移�??�????常設�? 2
    cv2.imshow('img',output2)
    cv2.imshow('img2',img_gray_copy)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break