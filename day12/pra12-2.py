import cv2

img = cv2.imread('D:/joker xue/4.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def empty(v):
    pass

cv2.namedWindow('Control')
cv2.createTrackbar('Blur','Control',0,20,empty)
cv2.createTrackbar('ksize','Control',0,21,empty)
cv2.createTrackbar('scale','Control',0,21,empty)

output = gray_img.copy()

while True:
    blur = cv2.getTrackbarPos('Blur','Control')
    ksize = cv2.getTrackbarPos('ksize','Control')
    scale = cv2.getTrackbarPos('scale','Control')
    if blur % 2 == 0:
            blur += 1
    blur_img = cv2.medianBlur(gray_img,blur)
    if ksize > 0 and scale > 0:
        if ksize % 2 == 0:
            ksize += 1
        if scale % 2 == 0:
            scale += 1
        output = cv2.Laplacian(blur_img,-1,ksize,scale)
        output_sob = cv2.Sobel(blur_img, -1, 1, 1, ksize,scale) 
        output_canny = cv2.Canny(blur_img,150,200) 
    else:
        output = blur_img.copy()
        output_sob = blur_img.copy()
        output_canny = blur_img.copy()
    output = cv2.cvtColor(output,cv2.COLOR_GRAY2BGR)

    cv2.imshow('ori_img',img)
    cv2.imshow('lap_img',output)
    cv2.imshow('sob_img',output_sob)
    cv2.imshow('canny_img',output_canny)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
