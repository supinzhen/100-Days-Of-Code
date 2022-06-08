import cv2
import numpy as np

img = cv2.imread('D:/joker xue/172825-1.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
output_abs = img.copy()

def empty(v):
    pass

cv2.namedWindow('Adjust')
cv2.createTrackbar('contrast','Adjust',100,200,empty)
cv2.createTrackbar('brightness','Adjust',100,200,empty)

while True:
    contrast = cv2.getTrackbarPos('contrast','Adjust') - 100
    brightness = cv2.getTrackbarPos('brightness','Adjust') -100
    output = img * (contrast/100 + 1) - contrast + brightness # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.convertScaleAbs(output, output_abs,2, 5)
    cv2.imshow('ori',img)
    cv2.imshow('output',output)
    cv2.imshow('output_abs',output_abs)
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break