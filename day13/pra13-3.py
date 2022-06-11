import cv2
from cv2 import THRESH_BINARY_INV
import numpy as np

logo = cv2.imread('D:/joker xue/dsp_logo.jpg')  
green_logo = np.empty((logo.shape[0],logo.shape[1],3),np.uint8)

green_logo[:,:,0] = 255

logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask1 = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY_INV)
ret, mask2 = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY)

logo = cv2.bitwise_and(logo,logo,mask=mask1)
green_logo = cv2.bitwise_and(green_logo,green_logo,mask=mask2)

output = cv2.add(logo,green_logo)

cv2.imshow('logo',output)
cv2.waitKey(0)
cv2.imwrite('dsp_logo_green.jpg',output)