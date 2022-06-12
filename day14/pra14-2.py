import cv2
import numpy as np

blue_lower = np.array([87,0,0])
blue_upper = np.array([170,68,120])

red_lower = np.array([0,0,149])
red_upper = np.array([115,68,215])

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if ret:
        blue_mask = cv2.inRange(frame,blue_lower,blue_upper)
        red_mask = cv2.inRange(frame,red_lower,red_upper)
        blue_output = cv2.bitwise_and(frame,frame,mask=blue_mask)
        red_output = cv2.bitwise_and(frame,frame,mask=red_mask)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        blue_output = cv2.dilate(blue_output,kernel)
        red_output = cv2.dilate(red_output,kernel)
        blue_output = cv2.erode(blue_output,kernel)
        red_output = cv2.erode(red_output,kernel)

        blue_output_gray = cv2.cvtColor(blue_output,cv2.COLOR_BGR2GRAY)
        red_output_gray = cv2.cvtColor(red_output,cv2.COLOR_BGR2GRAY) 

        blur_contour, hier = cv2.findContours(blue_output_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for con in blur_contour:
            area = cv2.contourArea(con)
            if area > 500:
                x,y,w,h = cv2.boundingRect(con)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        red_contour,hier = cv2.findContours(red_output_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for con in red_contour:
            area = cv2.contourArea(con)
            if area>500:
                x,y,w,h = cv2.boundingRect(con)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow('ori_video',frame)
    else:
        break
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break