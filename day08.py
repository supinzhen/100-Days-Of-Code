import cv2
import numpy as np
import pytesseract

cap = cv2.VideoCapture('result.mp4')
ret,frame1 = cap.read()
last_text = '--'

def empty(v):
    pass

cv2.namedWindow('crop/resize')
cv2.resizeWindow('crop/resize',560,320)

cv2.createTrackbar('crop x1','crop/resize',0,frame1.shape[1],empty)
cv2.createTrackbar('crop x2','crop/resize',frame1.shape[1],frame1.shape[1],empty)
cv2.createTrackbar('crop y1','crop/resize',0,frame1.shape[0],empty)
cv2.createTrackbar('crop y2','crop/resize',frame1.shape[0],frame1.shape[0],empty)
cv2.createTrackbar('resize(%)','crop/resize',100,1000,empty)

while True:
    x1 = cv2.getTrackbarPos('crop x1','crop/resize')
    x2 = cv2.getTrackbarPos('crop x2','crop/resize')
    y1 = cv2.getTrackbarPos('crop y1','crop/resize')
    y2 = cv2.getTrackbarPos('crop y2','crop/resize')
    percentage = float(cv2.getTrackbarPos('resize(%)','crop/resize'))
    new_img = frame1[y1:y2,x1:x2]
    new_img = cv2.resize(new_img,(0,0),fx=percentage/100,fy=percentage/100)

    cv2.imshow('img',new_img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

img = np.zeros((300,300,3),np.uint8)
black = img.copy()

while True:
    black = img.copy()
    new = ''
    ret,frame = cap.read()
    frame = frame[y1:y2,x1:x2]
    if ret:
        cv2.imshow('video',frame)
        text = pytesseract.image_to_string(frame)
        for i in range (5):
            if ord(text[i])>58 or ord(text[i])<48:
                new = last_text[:4]
                num = (int(last_text[3])-1)
                new = new+ str(num)
                text = new 
        if text != last_text:
            new = text
            last_text = new
            cv2.putText(black,'{}'.format(new),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
            print(new)
            cv2.imshow('black',black)
    else:
        break
    cmd = cv2.waitKey(1)
    if cmd == ord('q'):
        cv2.destroyAllWindows()
        break