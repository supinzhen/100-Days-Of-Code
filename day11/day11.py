from ast import Break
import cv2
from cv2 import blur
import numpy as np

img = cv2.imread('D:/joker xue/2.jpg')
img_copy = img.copy()

def empty(v):
    pass

cv2.namedWindow('Adjust')
cv2.resizeWindow('Adjust',600,300)
cv2.createTrackbar('Brightness','Adjust',100,200,empty)
cv2.createTrackbar('Contrast','Adjust',100,200,empty)
cv2.createTrackbar('Transhold','Adjust',0,1,empty)
cv2.createTrackbar('Transhld value','Adjust',127,255,empty)
cv2.createTrackbar('Blur','Adjust',0,11,empty)
cv2.createTrackbar('Median Blur','Adjust',0,11,empty)
cv2.createTrackbar('Negative','Adjust',0,1,empty)

while True:
    brightness = cv2.getTrackbarPos('Brightness','Adjust') - 100
    contrast = cv2.getTrackbarPos('Contrast','Adjust') -100
    output = img_copy * (contrast/100 + 1) - contrast + brightness
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    
    blur = cv2.getTrackbarPos('Blur','Adjust')
    if blur > 0:
        if blur%2==0:
            blur += 1 
        output = cv2.blur(output,(blur,blur))
    
    median_blur = cv2.getTrackbarPos('Median Blur','Adjust')
    if median_blur > 0:
        if median_blur%2==0:
            median_blur += 1 
        output = cv2.GaussianBlur(output,(median_blur,median_blur),0)
    
    neg = cv2.getTrackbarPos('Negative','Adjust')
    if neg == 1:
        output[:,:,:] = 255 - output[:,:,:]

    transhold = cv2.getTrackbarPos('Transhold','Adjust')
    if transhold == 1 :
        transhold_v = cv2.getTrackbarPos('Transhld value','Adjust')
        gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
        gray[:,:][gray[:,:]>transhold_v] = 255
        gray[:,:][gray[:,:]<=transhold_v] = 0
        output = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
        output = gray.copy()

    cv2.imshow('output',output)
    cv2.imshow('img',img)
    cmd = cv2.waitKey(1)
    if cmd == ord('q'):
        cv2.destroyAllWindows()
        break
    elif cmd == ord('w'):
        text = input('Please input filename:')
        while True:
            file_type = input('Please enter 1 for jpg file, 2 for png file:')
            if int(file_type) == 1:
                text += '.jpg'
                break
            elif int(file_type) == 2:
                text += '.png'
                break
            else:
                print('Wrong file type! Please try again.')
        cv2.imwrite(text,output)

