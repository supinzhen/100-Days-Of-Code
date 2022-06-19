import cv2
import numpy as np

img = cv2.imread('./dsp_logo_green.jpg')
key_empty = np.zeros((720,1280,3),np.uint8)
key_empty[:,:,:] = 255
key_sourse = img.copy()
key_sourse[:,:,:][key_sourse[:,:,0]>160] = 255
key_empty[:key_sourse.shape[0],:key_sourse.shape[1]] = key_sourse

gray_key_sourse = cv2.cvtColor(key_empty,cv2.COLOR_BGR2GRAY)
ret,mask1 = cv2.threshold(gray_key_sourse,200,500,cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(key_empty,key_empty, mask = mask1)

bg = np.zeros((720,1280,3),np.uint8)
bg[:,:,1] = 255
ret, mask2 = cv2.threshold(gray_key_sourse,200,500,cv2.THRESH_BINARY)
bg = cv2.bitwise_and(bg,bg,mask=mask2)

output = cv2.add(bg,logo)

cv2.imshow('logo',output)
cv2.waitKey(0)