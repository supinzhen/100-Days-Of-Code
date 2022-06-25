import cv2
import numpy as np
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt

img = cv2.imread('D:/joker xue/7face0602aa763bf-3.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_copy = img.copy()
result = img.copy()
result_copy = result.copy()

color = ('b','g','r')
plt.style.use('dark_background')
fig1 = plt.figure('Histogram')

x1,x2,y1,y2 = 0,img.shape[0],0,img.shape[1]

def empty(v):
    pass

def crop_create(v):
    global x1,x2,y1,y2,result,result_copy
    if v == 1:
        cv2.namedWindow('crop')
        cv2.createTrackbar('x1','crop',x1,img.shape[0],empty)
        cv2.createTrackbar('x2','crop',x2,img.shape[0],empty)
        cv2.createTrackbar('y1','crop',y1,img.shape[1],empty)
        cv2.createTrackbar('y2','crop',y2,img.shape[1],empty)
    else:
        cv2.destroyWindow('crop')
        result_copy = result.copy()

def bright_create(v):
    global result,result_copy
    if v == 1:
        cv2.namedWindow('brightness/contrast')
        cv2.createTrackbar('brightness','brightness/contrast',100,200,empty)
        cv2.createTrackbar('contrast','brightness/contrast',100,200,empty)
    else:
        cv2.destroyWindow('brightness/contrast')
        result_copy = result.copy()

cv2.namedWindow('adjust')
cv2.createTrackbar('crop','adjust',0,1,crop_create)
cv2.createTrackbar('brightness/contrast','adjust',0,1,bright_create)

while True:
    crop_power = cv2.getTrackbarPos('crop','adjust')
    bri_power = cv2.getTrackbarPos('brightness/contrast','adjust')

    if bri_power == 1:
        bri = cv2.getTrackbarPos('brightness','brightness/contrast') - 100
        con = cv2.getTrackbarPos('contrast','brightness/contrast') - 100
        result = result_copy * (con/100 + 1) - con + bri
        result = np.clip(result, 0, 255)
        result = np.uint8(result)

    if crop_power == 1:
        x1 = cv2.getTrackbarPos('x1','crop')
        x2 = cv2.getTrackbarPos('x2','crop')
        y1 = cv2.getTrackbarPos('y1','crop')
        y2 = cv2.getTrackbarPos('y2','crop')
        result = img_copy[x1:x2,y1:y2]

    cv2.imshow('img',img)
    cv2.imshow('result',result)
    cmd = cv2.waitKey(1)
    for idx, col in enumerate(color):
        histogram = cv2.calcHist([result],[idx],None,[256],[0, 256])
        plt.plot(histogram, color = col)
        plt.xlim([0, 256])
    plt.pause(0.1)
    fig1.clf()
    if cmd == ord('q'):
        cv2.destroyAllWindows()
        plt.ioff()
        break
    elif cmd == ord('w'):
        now = datetime.now()
        date = date.today()
        current_time = now.strftime("%H-%M-%S")
        current_date = date.strftime("%b-%d-%Y-")
        file_name = current_date + current_time + '.jpg'
        cv2.imwrite(file_name,result)
    elif cmd == ord('c'):
        result = img.copy()
        result_copy = img.copy()
