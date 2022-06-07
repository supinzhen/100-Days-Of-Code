import cv2
import numpy as np

img = cv2.imread('D:/joker xue/4e5e0002be56b88e3701.jfif')

img = img.astype(np.float32)
img = img/255.0

def empty(v):
    pass

cv2.namedWindow('Adjust')
cv2.createTrackbar('Hue','Adjust',18000,36000,empty)
cv2.createTrackbar('Lightness','Adjust',100,200,empty)
cv2.createTrackbar('Saturation','Adjust',100,200,empty)

ori_light = 100
ori_hue = 180
ori_sat = 100

re_img = img.copy()

while True:
    img_hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    hue = (cv2.getTrackbarPos('Hue','Adjust') - 18000)
    light = (cv2.getTrackbarPos('Lightness','Adjust') - 100)
    sat = (cv2.getTrackbarPos('Saturation','Adjust') - 100)
    img_hls[:, :, 0] = (1 + hue / 36000.0) * img_hls[:, :, 0]
    img_hls[:, :, 0][img_hls[:, :, 0] > 360] = 360 
    img_hls[:, :, 1] = (1 + light / 100.0) * img_hls[:, :, 1]
    img_hls[:, :, 1][img_hls[:, :, 1] > 1] = 1       
    img_hls[:, :, 2] = (1 + sat / 100.0) * img_hls[:, :, 2]
    img_hls[:, :, 2][img_hls[:, :, 2] > 1] = 1    
    ori_light = light
    ori_hue = hue
    ori_sat = sat
    re_img = cv2.cvtColor(img_hls,cv2.COLOR_HLS2BGR)
    re_img = ((re_img * 255).astype(np.uint8)) 
    cv2.imshow('before',img)
    cv2.imshow('after',re_img)

    if cv2.waitKey(1)==ord('q'): 
        cv2.destroyAllWindows()