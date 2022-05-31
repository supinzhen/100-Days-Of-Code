from ast import While
import cv2
import time
import numpy as np

def whiteBG(img):
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            img[row][col] = (255,255,255)

def ColorSet(img):
    cv2.namedWindow('ColorSet')
    cv2.resizeWindow('ColorSet',400,200)
    
    def empty(v):
        pass

    cv2.createTrackbar('R','ColorSet',0,255,empty)
    cv2.createTrackbar('G','ColorSet',0,255,empty)
    cv2.createTrackbar('B','ColorSet',0,255,empty)

    while True:
        r = cv2.getTrackbarPos('R','ColorSet')
        g = cv2.getTrackbarPos('G','ColorSet')
        b = cv2.getTrackbarPos('B','ColorSet')
        cv2.putText(img,'00:00:00',(50,200),cv2.FONT_ITALIC,3,(b,g,r),3)
        cv2.putText(img,'Set your countdown color!',(50,50),cv2.FONT_ITALIC,1,(b,g,r),1)
        cv2.putText(img,'Press \'q\' when you are done!',(50,100),cv2.FONT_ITALIC,1,(b,g,r),1)
        cv2.imshow('img',img)
        if cv2.waitKey(1)==ord('q'):
            cv2.destroyAllWindows()
            break
    return b,g,r

def CountDownThreeMinute(img,b,g,r):
    t = 5*30
    cv2.putText(img,'Count Down',(50,100),cv2.FONT_HERSHEY_PLAIN,2,(b,g,r),4)
    while t:
        mins = t// 30 // 60
        sec = t//30 % 60
        mini = t%30
        timer = '{:02d}:{:02d}:{:02d}'.format(mins,sec,mini)
        cv2.putText(img,timer,(50,250),cv2.FONT_ITALIC,3,(b,g,r),3)
        cv2.imshow('img',img)
        cv2.putText(img,timer,(50,250),cv2.FONT_ITALIC,3,(255,255,255),3)
        time.sleep(1/30)
        t-=1
        if cv2.waitKey(1)==ord('q'):
            cv2.destroyAllWindows()
            break
    cv2.putText(img,'Time\'s up!!',(50,250),cv2.FONT_ITALIC,3,(0,0,255),3)
    cv2.imshow('img',img)
    if cv2.waitKey(0)==ord('q'):
        cv2.destroyAllWindows()

bg = np.empty((300,600,3),np.uint8)
whiteBG(bg)
color_b,color_g,color_r = ColorSet(bg)
whiteBG(bg)
CountDownThreeMinute(bg,color_b,color_g,color_r)
