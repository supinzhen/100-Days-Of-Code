from ctypes.wintypes import PMSG
import cv2
import numpy as np

cap1 = cv2.VideoCapture('D:/joker xue/[ 纯享版 ] 林俊杰《输了你赢了世界又如何》《梦想的声音2》EP.4 20171124 _浙江卫视官方HD_.mp4')
cap2 = cv2.VideoCapture('D:/joker xue/【开场表演】薛之谦《你还要我怎样》《中国新歌声》中秋踢馆赛 SING!CHINA SP.1 20160915 [浙江卫视官方超清1080P].mp4')
cap3 = cv2.VideoCapture('D:/joker xue/田馥甄-演員.mp4')
cap4 = cv2.VideoCapture('D:/joker xue/【单曲纯享】张杰《星星》—《天籁之战2》第9期【东方卫视官方高清】.mp4')
cap5 = cv2.VideoCapture('D:/joker xue/薛之謙 live 王子公主.mp4')
cap6 = cv2.VideoCapture('D:/joker xue/张碧晨《你给我听好》-《歌手2017》第11期 单曲纯享版The Singer【我是歌手官方频道】.mp4')
cap7 = cv2.VideoCapture('D:/joker xue/【单曲纯享】《母系社会》范媛媛 《天籁之战》第9期【东方卫视官方高清】.mp4')
input8 = cv2.imread('./dsp_logo_green.jpg')

cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap3.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap4.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap5.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap5.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap6.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap6.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
cap7.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap7.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
input8 = cv2.resize(input8,(1280,720))
#cap8.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
#cap8.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

multi_view = np.zeros((720,1280,3),np.uint8)
multi_view_blank = multi_view.copy()
input1_v = np.zeros((171,304,3),np.uint8)
input2_v = np.zeros((171,304,3),np.uint8)
input3_v = np.zeros((171,304,3),np.uint8)
input4_v = np.zeros((171,304,3),np.uint8)
input5_v = np.zeros((171,304,3),np.uint8)
input6_v = np.zeros((171,304,3),np.uint8)
input7_v = np.zeros((171,304,3),np.uint8)
input8_v = np.zeros((171,304,3),np.uint8)

pgm = np.zeros((720,1280,3),np.uint8)
pvw = np.zeros((720,1280,3),np.uint8)

pgm_v = np.zeros((342,608,3),np.uint8)
pvw_v = np.zeros((342,608,3),np.uint8)

pvw_num = 0
pgm_num = 0
bar_last = 0
record = 0
cmd = 0
wipe_dir = 0
left = False
right = False

def call(event,x,y,flags,userdata):
    global pvw_num
    if event == 4:
        if 368<y<539 and 20<x<324:
            pvw_num = 1
        elif 368<y<539 and 324<x<628:
            pvw_num = 2
        elif 368<y<539 and 652<x<956:
            pvw_num = 3
        elif 368<y<539 and 956<x<1260:
            pvw_num = 4
        elif 539<y<710 and 20<x<324:
            pvw_num = 5
        elif 539<y<710 and 324<x<628:
            pvw_num = 6
        elif 539<y<710 and 652<x<956:
            pvw_num = 7
        elif 539<y<710 and 956<x<1260:
            pvw_num = 8

def cap_read():
    global ret1,ret2,ret3,ret4,ret5,ret6,ret7,ret8
    global input1,input2,input3,input4,input5,input6,input7,input8
    global input1_v,input2_v,input3_v,input4_v,input5_v,input6_v,input7_v,input8_v
    ret1, input1 = cap1.read()
    input1_v = cv2.resize(input1,(304,171))
    ret2, input2 = cap2.read()
    input2_v = cv2.resize(input2,(304,171))
    ret3, input3 = cap3.read()
    input3_v = cv2.resize(input3,(304,171))
    ret4, input4 = cap4.read()
    input4_v = cv2.resize(input4,(304,171))
    ret5, input5 = cap5.read()
    input5_v = cv2.resize(input5,(304,171))
    ret6, input6 = cap6.read()
    input6_v = cv2.resize(input6,(304,171))
    ret7, input7 = cap7.read()
    input7_v = cv2.resize(input7,(304,171))
    #ret8, input8 = cap8.read()
    input8_v = cv2.resize(input8,(304,171))

def pvw_num_judge():
    global pvw_v,pvw_num,pvw
    if pvw_num == 1:
        pvw_v = cv2.resize(input1,(608,342))
        pvw = cv2.resize(input1,(1280,720))
    elif pvw_num == 2:
        pvw_v = cv2.resize(input2,(608,342))
        pvw = cv2.resize(input2,(1280,720))
    elif pvw_num == 3:
        pvw_v = cv2.resize(input3,(608,342))
        pvw = cv2.resize(input3,(1280,720))
    elif pvw_num == 4:
        pvw_v = cv2.resize(input4,(608,342))
        pvw = cv2.resize(input4,(1280,720))
    elif pvw_num == 5:
        pvw_v = cv2.resize(input5,(608,342))
        pvw = cv2.resize(input5,(1280,720))
    elif pvw_num == 6:
        pvw_v = cv2.resize(input6,(608,342))
        pvw = cv2.resize(input6,(1280,720))
    elif pvw_num == 7:
        pvw_v = cv2.resize(input7,(608,342))
        pvw = cv2.resize(input7,(1280,720))
    elif pvw_num == 8:
        pvw_v = cv2.resize(input8,(608,342))
        pvw = cv2.resize(input8,(1280,720))
    else:
        pvw = np.zeros((720,1280,3),np.uint8)
        pvw_v = cv2.resize(pvw,(608,342))

def pgm_show():
    global pgm_num,pgm,pgm_v
    if pgm_num == 1:
        pgm_v = cv2.resize(input1,(608,342))
        pgm = cv2.resize(input1,(1280,720))
    elif pgm_num == 2:
        pgm_v = cv2.resize(input2,(608,342))
        pgm = cv2.resize(input2,(1280,720))
    elif pgm_num == 3:
        pgm_v = cv2.resize(input3,(608,342))
        pgm = cv2.resize(input3,(1280,720))
    elif pgm_num == 4:
        pgm_v = cv2.resize(input4,(608,342))
        pgm = cv2.resize(input4,(1280,720))
    elif pgm_num == 5:
        pgm_v = cv2.resize(input5,(608,342))
        pgm = cv2.resize(input5,(1280,720))
    elif pgm_num == 6:
        pgm_v = cv2.resize(input6,(608,342))
        pgm = cv2.resize(input6,(1280,720))
    elif pgm_num == 7:
        pgm_v = cv2.resize(input7,(608,342))
        pgm = cv2.resize(input7,(1280,720))
    elif pgm_num == 8:
        pgm_v = cv2.resize(input8,(608,342))
        pgm = cv2.resize(input8,(1280,720))
    else:
        pgm = np.zeros((720,1280,3),np.uint8)
        pgm_v = cv2.resize(pgm,(608,342))

def tolly_light():
    if pvw_num == 1:
        cv2.rectangle(multi_view,(20,368),(324,539),(0,255,0),2)
    elif pvw_num == 2:
        cv2.rectangle(multi_view,(324,368),(628,539),(0,255,0),2)
    elif pvw_num == 3:
        cv2.rectangle(multi_view,(652,368),(956,539),(0,255,0),2)
    elif pvw_num == 4:
        cv2.rectangle(multi_view,(956,368),(1260,539),(0,255,0),2)
    elif pvw_num == 5:
        cv2.rectangle(multi_view,(20,539),(324,710),(0,255,0),2)
    elif pvw_num == 6:
        cv2.rectangle(multi_view,(324,539),(628,710),(0,255,0),2)
    elif pvw_num == 7:
        cv2.rectangle(multi_view,(652,539),(956,710),(0,255,0),2)
    elif pvw_num == 8 :
        cv2.rectangle(multi_view,(956,539),(1260,710),(0,255,0),2)

    if pgm_num == 1:
        cv2.rectangle(multi_view,(20,368),(324,539),(0,0,255),2)
    if pgm_num == 2:
        cv2.rectangle(multi_view,(324,368),(628,539),(0,0,255),2)
    if pgm_num == 3:
        cv2.rectangle(multi_view,(652,368),(956,539),(0,0,255),2)
    if pgm_num == 4:
        cv2.rectangle(multi_view,(956,368),(1260,539),(0,0,255),2)
    if pgm_num == 5:
        cv2.rectangle(multi_view,(20,539),(324,710),(0,0,255),2)
    if pgm_num == 6:
        cv2.rectangle(multi_view,(324,539),(628,710),(0,0,255),2)
    if pgm_num == 7:
        cv2.rectangle(multi_view,(652,539),(956,710),(0,0,255),2)
    if pgm_num == 8 or key == 1:
        cv2.rectangle(multi_view,(956,539),(1260,710),(0,0,255),2)

def empty(v):
    pass

def wipe():
    global pgm_v,pvw_v
    trans_pvw[0:pgm.shape[0],0:bar] = pgm[0:pgm.shape[0],0:bar]
    trans_pgm[0:pgm.shape[0],0:bar] = pvw[0:pvw.shape[0],0:bar]
    cv2.line(trans_pgm,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
    cv2.line(trans_pvw,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
    pgm_v = cv2.resize(trans_pgm,(608,342))
    pvw_v = cv2.resize(trans_pvw,(608,342))
    
def key_on():
    global pgm,pgm_v,pvw,pvw_v
    key_empty = np.zeros((720,1280,3),np.uint8)
    key_empty[:,:,:] = 255
    key_sourse = input8.copy()
    key_sourse[:,:,:][key_sourse[:,:,0]>160] = 255
    key_empty[:key_sourse.shape[0],:key_sourse.shape[1]] = key_sourse

    gray_key_sourse = cv2.cvtColor(key_empty,cv2.COLOR_BGR2GRAY)
    ret,mask1 = cv2.threshold(gray_key_sourse,200,500,cv2.THRESH_BINARY_INV)
    logo = cv2.bitwise_and(key_empty,key_empty, mask = mask1)

    ret, mask2 = cv2.threshold(gray_key_sourse,200,500,cv2.THRESH_BINARY)
    pvw = cv2.bitwise_and(pvw,pvw,mask=mask2)
    pgm = cv2.bitwise_and(pgm,pgm,mask=mask2)

    pgm = cv2.add(pgm,logo)
    pvw = cv2.add(pvw,logo)

    pgm_v = cv2.resize(pgm,(608,342))
    pvw_v = cv2.resize(pvw,(608,342))


cv2.namedWindow('control')
cv2.resizeWindow('control',(600,150))
cv2.createTrackbar('T-bar','control',pgm.shape[1],pgm.shape[1],empty)
cv2.createTrackbar('key','control',0,1,empty)

while True:
    cap_read()
    if ret1 and ret2 and ret3 and ret4:
        cut = False
        multi_view = multi_view_blank.copy()
        pvw_num_judge()
        pgm_show()

        #key
        key = cv2.getTrackbarPos('key','control')
        if key == 1:
            key_on()


        #wipe 
        trans_pgm = pgm.copy()
        trans_pvw = pvw.copy()
        bar = cv2.getTrackbarPos('T-bar','control')
        if wipe_dir == 1 and bar!=pgm.shape[1]: #Right to left
            trans_pvw[0:pgm.shape[0],bar:pgm.shape[1]] = pgm[0:pgm.shape[0],bar:pgm.shape[1]]
            trans_pgm[0:pgm.shape[0],bar:pgm.shape[1]] = pvw[0:pvw.shape[0],bar:pgm.shape[1]]
            cv2.line(trans_pgm,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
            cv2.line(trans_pvw,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
            pgm_v = cv2.resize(trans_pgm,(608,342))
            pvw_v = cv2.resize(trans_pvw,(608,342))
            if bar == 0:
                left = True
        elif wipe_dir == 2 and bar !=0: #left to right
            trans_pvw[0:pgm.shape[0],0:bar] = pgm[0:pgm.shape[0],0:bar]
            trans_pgm[0:pgm.shape[0],0:bar] = pvw[0:pvw.shape[0],0:bar]
            cv2.line(trans_pgm,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
            cv2.line(trans_pvw,(bar,0),(bar,trans_pgm.shape[0]),(255,255,255),5)
            pgm_v = cv2.resize(trans_pgm,(608,342))
            pvw_v = cv2.resize(trans_pvw,(608,342))
            if bar == pgm.shape[1]:
                right = True
        if bar == 0: #Left to right
            left = True
            wipe_dir = 2
        elif bar==pgm.shape[1]: #Right to left
            right = True
            wipe_dir = 1
        if left == True and right == True :
            cut = True
            left = False
            right = False



        multi_view[10:352,20:628] = pvw_v
        multi_view[10:352,652:1260] = pgm_v
        multi_view[368:539,20:324] = input1_v
        multi_view[368:539,324:628] = input2_v
        multi_view[368:539,652:956] = input3_v
        multi_view[368:539,956:1260] = input4_v
        multi_view[539:710,20:324] = input5_v
        multi_view[539:710,324:628] = input6_v
        multi_view[539:710,652:956] = input7_v
        multi_view[539:710,956:1260] = input8_v
        tolly_light()
        cv2.putText(multi_view,'Program',(880,352),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1)
        cv2.putText(multi_view,'Preview',(230,352),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1)
    else:
        break

    cv2.imshow('multi viewer',multi_view)
    cv2.setMouseCallback('multi viewer',call)
    cmd = cv2.waitKey(30)
    
    if cmd == ord(' ') or cmd == ord('c') or cut == True:
        pvw,pgm = pgm,pvw
        pvw_num,pgm_num = pgm_num,pvw_num

    if cmd == ord('1'):
        pvw_num = 1
    if cmd == ord('2'):
        pvw_num = 2
    if cmd == ord('3'):
        pvw_num = 3
    if cmd == ord('4'):
        pvw_num = 4
    if cmd == ord('5'):
        pvw_num = 5
    if cmd == ord('6'):
        pvw_num = 6
    if cmd == ord('7'):
        pvw_num = 7
    if cmd == ord('8'):
        pvw_num = 8
    
    if  cmd == ord('q'):
        cv2.destroyAllWindows()
        break


