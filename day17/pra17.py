import cv2
import numpy as np

w = 400
h = 400
r = 200

def show_xy(event,x,y,flag,userdata):
    global img
    if event == 4:
        img = np.zeros((400,400,3),np.uint8)
        h = x
        w = y
        for i in range (400):
            for j in range(400):
                img[i,j,0] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(300*(2**0.5))*255
                img[i,j,1] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(300*(2**0.5))*255
                img[i,j,2] =  int(((i-h)*(i-h)+(j-w)*(j-w))**0.5)/(300*(2**0.5))*255

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img',show_xy)

while True:
    #img = img.astype('float32')/255
    cv2.imshow('img',img)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break