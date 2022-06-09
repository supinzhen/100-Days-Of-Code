import cv2
import numpy as np

img = cv2.imread('D:/joker xue/349e-fypsqka4331768.jpg')
green = cv2.imread('D:/joker xue/349e-fypsqka4331768.jpg')


output = cv2.add(img,green)
output2 = cv2.addWeighted(img,0.8,green,0.6,0)
output3 = cv2.subtract(img,green)

cv2.imshow('output',output)
cv2.imshow('output2',output2)
cv2.imshow('output3',output3)


cv2.waitKey(0)