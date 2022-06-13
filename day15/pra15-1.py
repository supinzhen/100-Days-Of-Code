import cv2
import numpy as np

cap1 = cv2.VideoCapture('D:/joker xue/张碧晨《你给我听好》-《歌手2017》第11期 单曲纯享版The Singer【我是歌手官方频道】.mp4')
cap2 = cv2.VideoCapture('D:/joker xue/薛之謙 live 王子公主.mp4')

while True:
    ret ,frame1 = cap1.read()
    frame1 = cv2.resize(frame1,(360,240))
    ret, frame2 = cap2.read()
    frame2[10:250,10:370] = frame1
    cv2.rectangle(frame2,(10,10),(370,250),(255,255,255),2)

    cv2.imshow('video',frame2)

    if cv2.waitKey(30) == ord('q'):
        cv2.destroyAllWindows()
        break