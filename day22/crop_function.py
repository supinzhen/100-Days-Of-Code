import cv2
import numpy as np

img = cv2.imread('D:/joker xue/4.jpg')
img_white = img.copy()
img_temp = img_white.copy()
img_last = img.copy()

def show_xy(event,x,y,flag,userdata):
    global x1,y1,x2,y2,img
    if event == 1:
        x1 = x
        y1 = y
        cv2.circle(img,(x1,y1),1,(0,0,255),2)
    elif event == 4:
        x2 = x
        y2 = y
        if x1<x2 and y1<y2:
            blur = img_last[y1:y2,x1:x2]
            blur = cv2.GaussianBlur(blur,(9,9),15)
            img_last[y1:y2,x1:x2] = blur
        elif x2<x1 and y2<y1:
            blur = img_last[y2:y1,x2:x1]
            blur = cv2.GaussianBlur(blur,(9,9),15)
            img_last[y2:y1,x2:x1] = blur
        elif x2<x1 and y1<y2:
            blur = img_last[y1:y2,x2:x1]
            blur = cv2.GaussianBlur(blur,(9,9),15)
            img_last[y1:y2,x2:x1] = blur
        elif x2>x1 and y2<y1:
            blur = img_last[y2:y1,x1:x2]
            blur = cv2.GaussianBlur(blur,(9,9),15)
            img_last[y2:y1,x1:x2] = blur
        img = img_last.copy()
    elif event == 0 and flag ==1:
        current_x = x
        current_y = y
        img_temp = img_last.copy()
        cv2.rectangle(img_temp,(x1,y1),(current_x,current_y),(0,0,255),3)
        img = img_temp.copy()

while True:
    cv2.imshow('img',img)
    cv2.setMouseCallback('img',show_xy)
    cmd = cv2.waitKey(1)
    if cmd == ord('c'):
        img = img_white.copy()
        img_last = img.copy()
    elif cmd == ord('q'):
        cv2.imwrite('blur_img.jpg',img)
        cv2.destroyAllWindows()
        break