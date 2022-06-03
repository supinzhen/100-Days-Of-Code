import cv2
from cv2 import VideoCapture
from cv2 import INTER_CUBIC
import numpy as np

cap1 = cv2.VideoCapture('D:/joker xue/[ 纯享版 ] 林俊杰《输了你赢了世界又如何》《梦想的声音2》EP.4 20171124 _浙江卫视官方HD_.mp4')
cap2 = cv2.VideoCapture('D:/joker xue/【开场表演】薛之谦《你还要我怎样》《中国新歌声》中秋踢馆赛 SING!CHINA SP.1 20160915 [浙江卫视官方超清1080P].mp4')
cap3 = cv2.VideoCapture('D:/joker xue/田馥甄-演員.mp4')
cap4 = cv2.VideoCapture('D:/joker xue/畢書盡 Bii - 逆時光的浪 Back In Time (官方版MV) -  台視、三立、東森偶像劇「愛上哥們」前導篇「逆光」主題曲.mp4')

cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap3.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap4.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (360, 240))

bar = np.zeros((20,720,3),np.uint8)
gap = np.zeros((5,720,3),np.uint8)

pgm = np.zeros((240,360,3),np.uint8)
pvw = np.zeros((240,360,3),np.uint8)
pvw_num = 0
pgm_num = 0
record = 0
cmd = 0

def call(event,x,y,flags,userdata):
    global pvw,pvw_num
    if event == 4:
        if 0<x<180 and y>240:
            pvw_num = 1
        elif 180<x<360 and y>240:
            pvw_num = 2
        elif 360<x<540 and y>240:
            pvw_num = 3
        elif 540<x<720 and y>240 :
            pvw_num = 4

cv2.namedWindow('window')
cv2.setMouseCallback('window',call)


while True:
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    ret3,frame3 = cap3.read()
    ret4,frame4 = cap4.read()
    bar = np.zeros((20,720,3),np.uint8)
    cv2.putText(bar,'PREVIEW                     PROGRAM',(140,18),cv2.FONT_HERSHEY_COMPLEX,0.75,(255,255,255),2)
    if ret1 and ret2 and ret3 and ret4:
        img1_pre = cv2.resize(frame1,(180,120),interpolation=INTER_CUBIC)
        img2_pre = cv2.resize(frame2,(180,120),interpolation=INTER_CUBIC)
        img3_pre = cv2.resize(frame3,(180,120),interpolation=INTER_CUBIC)
        img4_pre = cv2.resize(frame4,(180,120),interpolation=INTER_CUBIC)
        if pvw_num == 1 or cmd == ord('1'):
            pvw = cv2.resize(frame1,(360,240),interpolation=INTER_CUBIC)
            pvw_num = 1
            cv2.rectangle(img1_pre,(0,0),(180,120),(0,255,0),3)
        elif pvw_num == 2 or cmd == ord('2'):
            pvw = cv2.resize(frame2,(360,240),interpolation=INTER_CUBIC)
            pvw_num = 2
            cv2.rectangle(img2_pre,(0,0),(180,120),(0,255,0),3)
        elif pvw_num == 3 or cmd == ord('3'):
            pvw = cv2.resize(frame3,(360,240),interpolation=INTER_CUBIC)
            pvw_num = 3
            cv2.rectangle(img3_pre,(0,0),(180,120),(0,255,0),3)
        elif pvw_num == 4 or cmd == ord('4'):
            pvw = cv2.resize(frame4,(360,240),interpolation=INTER_CUBIC)
            pvw_num = 4
            cv2.rectangle(img4_pre,(0,0),(180,120),(0,255,0),3)
        else:
            pvw = np.zeros((240,360,3),np.uint8)
        if pgm_num == 1:
            pgm = cv2.resize(frame1,(360,240),interpolation=INTER_CUBIC)
            cv2.rectangle(img1_pre,(0,0),(180,120),(0,0,255),3)
        elif pgm_num == 2:
            pgm = cv2.resize(frame2,(360,240),interpolation=INTER_CUBIC) 
            cv2.rectangle(img2_pre,(0,0),(180,120),(0,0,255),3)
        elif pgm_num == 3:
            pgm = cv2.resize(frame3,(360,240),interpolation=INTER_CUBIC)
            cv2.rectangle(img3_pre,(0,0),(180,120),(0,0,255),3)
        elif pgm_num == 4:
            pgm = cv2.resize(frame4,(360,240),interpolation=INTER_CUBIC)
            cv2.rectangle(img4_pre,(0,0),(180,120),(0,0,255),3)
        else:
            pgm = np.zeros((240,360,3),np.uint8)
        if record == 1:
            out.write(pgm)
            cv2.putText(bar,'Recording...',(330,18),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
        else:
            cv2.putText(bar,'Not Recording...',(300,18),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
        cv2.rectangle(pgm,(0,0),(360,240),(0,0,255),3)
        cv2.rectangle(pvw,(0,0),(360,240),(0,255,0),3)
        view = np.hstack((pvw,pgm))
        source = np.hstack((img1_pre,img2_pre,img3_pre,img4_pre))
        window = np.vstack((bar,view,gap,source))
        cv2.imshow('window',window)
        cmd = cv2.waitKey(25)
    if cmd == ord(' '):
        pvw,pgm = pgm,pvw
        pvw_num,pgm_num = pgm_num,pvw_num
    elif cmd == ord('r'):
        record = 1
    elif cmd == ord('e'):
        record = 0
        out.release()
    elif cmd == ord('q'):
        cap1.release()
        cap2.release()
        cap3.release()
        cap4.release()
        out.release()
        cv2.destroyAllWindows()
        break