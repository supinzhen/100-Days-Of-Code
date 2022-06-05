import cv2
import numpy as np
import pytesseract

img = cv2.imread('D:/Python/day07/2.png')

paper = np.empty((600,1000,3),np.uint8)
console = np.zeros((300,600,3),np.uint8)
ident = np.empty((200,300,3),np.uint8)

for row in range(200):
    for col in range(300):
        ident[row][col] = (255,255,255)

for row in range(600):
    for col in range(1000):
        paper[row][col] = (255,255,255)

img_white = img.copy()
img_temp = img.copy()
ident_white = ident.copy()

def show_xy(event,x,y,flag,userdata):
    global x1,y1,x2,y2,ident
    if event == 1:
        x1 = x
        y1 = y
        cv2.circle(img,(x1,y1),1,(0,0,255),2)
        cv2.imshow('img',img)
    elif event == 4:
        x2 = x
        y2 = y
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),3)
        ident = ident_white.copy()
        ident = img[y1:y2,x1:x2]
        text = pytesseract.image_to_string(ident,lang = 'chi_tra+eng')
        cv2.imshow('ident',ident)
        print(text)
    elif event == 0 and flag ==1:
        current_x = x
        current_y = y
        img_temp = img.copy()
        cv2.rectangle(img_temp,(x1,y1),(current_x,current_y),(0,0,255),3)
        cv2.imshow('img',img_temp)

while True:
    cv2.imshow('img',img)
    cv2.setMouseCallback('img',show_xy)
    cmd = cv2.waitKey(0)
    if cmd == ord('c'):
        img = img_white.copy()
    elif cmd == ord('q'):
        cv2.destroyAllWindows()
        break