import cv2
import numpy as np

img = cv2.imread('D:/joker xue/5.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)

h = img.shape[0]
w = img.shape[1]

a = 30
r = img[0,img.shape[1]-1,2]
g = img[0,img.shape[1]-1,1]
b = img[0,img.shape[1]-1,0]

for i in range(w):
    for j in range(h):
        r_cur = img[j,i,2]
        g_cur = img[j,i,1]
        b_cur = img[j,i,0]
        if r_cur>(r-a) and r_cur<(r+a)and g_cur>(g-a) and g_cur<(g+a) and b_cur>(b-a) and b_cur<(b+a):
            img[j,i,0] = 2
            img[j,i,1] = 200
            img[j,i,2] = 20

cv2.imshow('img',img)

if cv2.waitKey(0) == ord('q'):
    cv2.imwrite('img.png',img)
    cv2.destroyAllWindows()