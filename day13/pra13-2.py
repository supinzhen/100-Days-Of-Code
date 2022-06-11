import cv2
import numpy as np

logo = cv2.imread('D:/joker xue/dsp_logo.jpg')  
logo = cv2.resize(logo,(0,0),fx=0.5,fy=0.5)
logo_copy = logo.copy()

img = cv2.imread('D:/joker xue/6.jpg')
img_copy = img.copy()

def empty(v):
    pass

cv2.namedWindow('Crop')
cv2.createTrackbar('x1','Crop',0,logo.shape[0],empty)
cv2.createTrackbar('x2','Crop',logo.shape[0],logo.shape[0],empty)
cv2.createTrackbar('y1','Crop',0,logo.shape[1],empty)
cv2.createTrackbar('y2','Crop',logo.shape[1],logo.shape[1],empty)
cv2.createTrackbar('scale','Crop',100,200,empty)

while True:
    logo = logo_copy.copy()
    x1 = cv2.getTrackbarPos('x1','Crop')
    x2 = cv2.getTrackbarPos('x2','Crop')
    y1 = cv2.getTrackbarPos('y1','Crop')
    y2 = cv2.getTrackbarPos('y2','Crop')
    logo = logo[x1:x2,y1:y2]
    cv2.imshow('logo',logo)
    if cv2.waitKey(1) == ord('q'):
        print(x1,x2,y1,y2)
        cv2.destroyAllWindows()
        break

paper = np.empty((img.shape[0],img.shape[1],3),np.uint8)
paper[:,:,:] = 255
paper_white = paper.copy()

cv2.namedWindow('logo position')
cv2.createTrackbar('x','logo position',0,paper.shape[0] - logo.shape[0],empty)
cv2.createTrackbar('y','logo position',0,paper.shape[1] - logo.shape[1],empty)

x = 0
y = 0

while True:
    img = img_copy.copy()
    paper = paper_white.copy()
    x = cv2.getTrackbarPos('x','logo position')
    y = cv2.getTrackbarPos('y','logo position')
    x_end = (logo.shape[0] + x)
    y_end = (logo.shape[1] + y)
    paper[x:x_end,y:y_end,:] = logo
    
    logo_gray = cv2.cvtColor(paper,cv2.COLOR_BGR2GRAY)
    ret,mask1 = cv2.threshold(logo_gray,200, 255,cv2.THRESH_BINARY_INV)

    output = cv2.bitwise_and(paper,paper,mask=mask1)

    ret,mask2 = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY)
    img = cv2.bitwise_and(img,img,mask=mask2)

    output2 = cv2.add(img,output)

    cv2.imshow('logo',output2)
    if cv2.waitKey(1) == ord('q'):
        print(x,y)
        cv2.destroyAllWindows()
        break
