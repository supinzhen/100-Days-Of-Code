import cv2

img = cv2.imread('D:/joker xue/9-1.jpg')
img_copy = img.copy()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

erode_img = cv2.erode(img,kernel)
dilate_img = cv2.dilate(img,kernel)
#透過侵蝕與膨脹，去除影像中的雜訊


cv2.imshow('ori_img',img_copy)
cv2.imshow('erode_img',erode_img)
cv2.imshow('dilate_img',dilate_img)

cv2.waitKey(0)