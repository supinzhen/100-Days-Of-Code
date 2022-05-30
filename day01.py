import cv2

img = cv2.imread('xaT5UD3.jpg')

def empty(v):
    pass

cv2.namedWindow('crop/resize')
cv2.resizeWindow('crop/resize',560,320)

cv2.createTrackbar('crop x1','crop/resize',0,img.shape[1],empty)
cv2.createTrackbar('crop x2','crop/resize',img.shape[1],img.shape[1],empty)
cv2.createTrackbar('crop y1','crop/resize',0,img.shape[0],empty)
cv2.createTrackbar('crop y2','crop/resize',img.shape[0],img.shape[0],empty)
cv2.createTrackbar('resize(%)','crop/resize',100,1000,empty)

while True:
    x1 = cv2.getTrackbarPos('crop x1','crop/resize')
    x2 = cv2.getTrackbarPos('crop x2','crop/resize')
    y1 = cv2.getTrackbarPos('crop y1','crop/resize')
    y2 = cv2.getTrackbarPos('crop y2','crop/resize')
    percentage = float(cv2.getTrackbarPos('resize(%)','crop/resize'))
    new_img = img[y1:y2,x1:x2]
    new_img = cv2.resize(new_img,(0,0),fx=percentage/100,fy=percentage/100)

    cv2.imshow('img',new_img)
    cv2.waitKey(1)