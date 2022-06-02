import cv2

cap = cv2.VideoCapture('D:/Python/天涯客.mp4')

img = cv2.imread('D:/Python/beard-example-before@3x.jpg')
faceCas = cv2.CascadeClassifier('face_detect.xml') #載入模型
#640*480
ret,frame = cap.read()
x1 = frame.shape[1]//2-160
x2 = frame.shape[1]//2+160
y1 = frame.shape[0]//2-120
y2 = frame.shape[0]//2+120
while True:
    ret,frame = cap.read()
    if ret:
        faceRect = faceCas.detectMultiScale(frame,1.3,8)
        if len(faceRect)>0:
            for (x,y,w,h) in faceRect:

                    x1 = x+w//2-160
                    x2 = x+160+w//2
                    y1 = y+h//2-120
                    y2 = y+120+h//2
                    if y2>240 or x2>320:
                        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)

                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
        if y1<0 :
            result = frame[0:y2,x1:x2]
        elif x1<0:
            result = frame[y1:y2,0:x2]
        else:
            result = frame[y1:y2,x1:x2]
        cv2.imshow('result',result)
        cv2.imshow('frame',frame)
    else:
        break
    if cv2.waitKey(5) == ord('q'):
        cv2.destroyAllWindows()
        break