import cv2
import numpy as np
from PIL import Image

cap = cv2.VideoCapture('D:/joker xue/giphy.gif')
output = []
while True:
    ret,frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGRA2RGBA)
        img = Image.fromarray(img)
        img = img.convert('RGB')
        output.append(img)
        show = np.array(img,dtype=np.uint8)
        show = cv2.cvtColor(show,cv2.COLOR_RGB2BGR)
        cv2.imshow('video',show)
    else:
        break
    if cv2.waitKey(150) == ord('q'):
        break

output[1].save('test2.gif',save_all=True,append_images=output[1:],duration=150,loop=0,disposal=2)
cv2.destroyAllWindows()