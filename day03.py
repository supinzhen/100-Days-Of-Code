import cv2
import numpy as np

first = cv2.VideoCapture('D:/joker xue/170224 薛之谦 ——《说谎》（超强音浪）.mp4')
second = cv2.VideoCapture('D:/joker xue/【开场表演】薛之谦《你还要我怎样》《中国新歌声》中秋踢馆赛 SING!CHINA SP.1 20160915 [浙江卫视官方超清1080P].mp4')

ret_1 ,frame_1 = first.read()
ret_2 ,frame_2 = second.read()

def empty(v):
    pass

cv2.namedWindow('control')
cv2.createTrackbar('bar','control',frame_1.shape[1],frame_1.shape[1],empty)

while True:
    ret_1 ,frame_1 = first.read()
    result = frame_1.copy()
    p = cv2.getTrackbarPos('bar','control')
    if p == frame_1.shape[1]:
        second = cv2.VideoCapture('D:/joker xue/【开场表演】薛之谦《你还要我怎样》《中国新歌声》中秋踢馆赛 SING!CHINA SP.1 20160915 [浙江卫视官方超清1080P].mp4')
        result = frame_1.copy()
    elif p != 0 :
        ret_2 ,frame_2 = second.read()
        frame_1 = frame_1[0:frame_1.shape[0],0:p]
        frame_2 = frame_2[0:frame_2.shape[0],p:frame_2.shape[1]]
        result = np.hstack((frame_1,frame_2))
        cv2.line(result,(p,0),(p,frame_1.shape[0]),(255,255,255),2)
    elif p==0:
        first = cv2.VideoCapture('D:/joker xue/170224 薛之谦 ——《说谎》（超强音浪）.mp4')
        ret_2 ,frame_2 = second.read()
        result = frame_2.copy()
    result = cv2.resize(result,(0,0),fx=0.5,fy=0.5)
    cv2.imshow('result',result)
    if cv2.waitKey(25)==ord('q'):
        cv2.destroyWindow()
