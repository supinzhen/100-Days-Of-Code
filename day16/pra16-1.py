from PIL import Image,ImageSequence
import cv2
import numpy as np

gif = Image.open('D:/joker xue/giphy (1).gif')

img_list = []

for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')
    opencv_img = np.array(frame,dtype=np.uint8)
    opencv_img = cv2.cvtColor(opencv_img,cv2.COLOR_RGB2BGRA)

    cv2.rectangle(opencv_img,(100,160),(300,200),(0,0,0),-1)

    img_list.append(opencv_img)

loop = True
while loop:
    for i in img_list:
        cv2.imshow('gif',i)
        if cv2.waitKey(30)==ord('q'):
            loop = False
            break

#建立要輸出的影格串列
output = []
for i in img_list :
    img = i
    img = cv2.cvtColor(img,cv2.COLOR_BGRA2RGBA) #因為opencv是BGRA因此要轉換成RGBA
    img = Image.fromarray(img) #轉換成PIL格式
    img = img.convert('RGB')   #轉換成RGB(RGBA會自動把黑色白色變成透明色)
    output.append(img)         #加入output

#儲存為gif動畫圖檔
output[0].save('next_gif.gif',save_all = True,append_images = output[1:],duration=200,loop=0,disposal=0)

cv2.destroyAllWindows()