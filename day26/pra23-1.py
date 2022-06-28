import cv2
import numpy as np
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt

img = cv2.imread('D:/joker xue/27751895_2005396873048080_5171564001063606625_n.jpg')
#img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
edit_window = np.zeros((img.shape[0]+80,img.shape[1]*2,3),np.uint8)
img_copy = img.copy()
result = img.copy()

color = ('b','g','r')
plt.style.use('dark_background')
fig1 = plt.figure('Histogram')

x1,x2,y1,y2 = 0,img.shape[0],0,img.shape[1]
r,g,b,opacity = 0,0,50,0
bri,con = 0,0
negative = 0

def histogram_generate():
    for idx, col in enumerate(color):
        histogram = cv2.calcHist([result],[idx],None,[256],[0, 256])
        plt.plot(histogram, color = col)
        plt.xlim([0, 256])
    plt.pause(0.1)
    fig1.clf()

def empty(v):
    pass

def crop_create(v):
    global x1,x2,y1,y2
    if v == 1:
        cv2.namedWindow('crop')
        cv2.resizeWindow('crop',600,300)
        cv2.createTrackbar('x1','crop',x1,img.shape[0]-1,empty)
        cv2.createTrackbar('x2','crop',x2,img.shape[0]-1,empty)
        cv2.createTrackbar('y1','crop',y1,img.shape[1]-1,empty)
        cv2.createTrackbar('y2','crop',y2,img.shape[1]-1,empty)
    else:
        cv2.destroyWindow('crop')

def bright_create(v):
    global con,bri
    if v == 1:
        cv2.namedWindow('brightness/contrast')
        cv2.resizeWindow('brightness/contrast',600,300)
        cv2.createTrackbar('brightness','brightness/contrast',bri+100,200,empty)
        cv2.createTrackbar('contrast','brightness/contrast',con+100,200,empty)
    else:
        cv2.destroyWindow('brightness/contrast')

def filter_create(v):
    global r,g,b,opacity
    if v == 1:
        cv2.namedWindow('filter')
        cv2.resizeWindow('filter',600,300)
        cv2.createTrackbar('r','filter',r,255,empty)
        cv2.createTrackbar('g','filter',g,255,empty)
        cv2.createTrackbar('b','filter',b,255,empty)
        cv2.createTrackbar('opacity','filter',opacity,100,empty)
    else:
        cv2.destroyWindow('filter')

def negative_create(v):
    global negative
    if v == 1:
        cv2.namedWindow('negative')
        cv2.resizeWindow('negative',600,300)
        cv2.createTrackbar('off/on','negative',negative,1,empty)
    else:
        cv2.destroyWindow('negative')

def con_bri_generate(img):
    #brightness/contrast
    img_copy = img * (con/100 + 1) - con + bri
    img_copy = np.clip(img_copy, 0, 255)
    img_copy = np.uint8(img_copy)
    return img_copy

def filter_generate(img,b,g,r,opacity):
    #filter
    filter_paper = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    filter_paper[:,:,0] = b
    filter_paper[:,:,1] = g
    filter_paper[:,:,2] = r
    img_copy[:,:,:] = img[:,:,:]*((100-opacity)/100) + filter_paper[:,:,:]*(opacity/100)
    return img_copy

def pvw_window(result):
    pvw = np.zeros((img.shape[0],img.shape[1],3),np.uint8) #create a preview window
    center_x = img.shape[0]//2
    center_y = img.shape[1]//2 
    start_x = center_x-result.shape[0]//2
    end_x = center_x+result.shape[0]-result.shape[0]//2
    start_y = center_y-result.shape[1]//2
    end_y = center_y+result.shape[1]-result.shape[1]//2
    pvw[start_x:end_x,start_y:end_y] = result
    edit_window[40:img.shape[0]+40,:img.shape[1]]= img
    edit_window[40:img.shape[0]+40,img.shape[1]:]= pvw
    cv2.putText(edit_window,'Original image',(pvw.shape[1]//4-50,30),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
    cv2.putText(edit_window,'Result',(pvw.shape[1]*3//2-50,30),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
    return edit_window

cv2.namedWindow('adjust',cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('adjust',600,300)
cv2.createTrackbar('crop','adjust',0,1,crop_create)
cv2.createTrackbar('brightness/contrast','adjust',0,1,bright_create)
cv2.createTrackbar('filter','adjust',0,1,filter_create)
cv2.createTrackbar('negative','adjust',0,1,negative_create)

while True:
    crop_power = cv2.getTrackbarPos('crop','adjust')
    bri_power = cv2.getTrackbarPos('brightness/contrast','adjust')
    filter_power = cv2.getTrackbarPos('filter','adjust')
    negative_power = cv2.getTrackbarPos('negative','adjust')
    img_copy = img.copy()


    if bri_power == 1:
        bri = cv2.getTrackbarPos('brightness','brightness/contrast') - 100
        con = cv2.getTrackbarPos('contrast','brightness/contrast') - 100

    if crop_power == 1:
        x1 = cv2.getTrackbarPos('x1','crop')
        x2 = cv2.getTrackbarPos('x2','crop')
        y1 = cv2.getTrackbarPos('y1','crop')
        y2 = cv2.getTrackbarPos('y2','crop')
    
    if filter_power == 1:
        r = cv2.getTrackbarPos('r','filter')
        g = cv2.getTrackbarPos('g','filter')
        b = cv2.getTrackbarPos('b','filter')
        opacity = cv2.getTrackbarPos('opacity','filter')
    
    if negative_power == 1:
        negative = cv2.getTrackbarPos('off/on','negative')
    
    #started to edit photo
    #brightness,contrast
    if con != 0 or bri != 0:
        img_copy = con_bri_generate(img_copy)
    
    #filter
    if opacity!= 0:
        img_copy = filter_generate(img_copy,b,g,r,opacity)

    #crop
    result = img_copy[x1:x2,y1:y2]

    #negative image
    if negative == 1:
        result[:,:,:] = 255 - result[:,:,:]

    #edit window 
    edit_window = pvw_window(result)

    cv2.imshow('Annie\'s Photo Editor',edit_window)

    #control
    cmd = cv2.waitKey(1)
    if cmd == ord('w'):
        file_name = input('Please enter filename:')
        cv2.imwrite(file_name + '.jpg',result)
        print('file saved.')
    if cmd == ord('r'):
        x1,x2,y1,y2 = 0,img.shape[0],0,img.shape[1]
        r,g,b,opacity = 0,0,50,0
        bri,con = 0,0
        negative = 0
    if cmd == ord('q'):
        cv2.destroyAllWindows()
        break