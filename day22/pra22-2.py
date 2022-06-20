import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:/joker xue/4.jpg')

color = ('b','g','r')
plt.style.use('dark_background')
plt.figure(figsize=(10,5))

for idx, color in enumerate(color):
    histogram = cv2.calcHist([img],[idx],None,[256],[0, 256])
    plt.plot(histogram, color = color)
    plt.xlim([0, 256])
plt.plot(histogram, color = color)
plt.xlim([0, 256])

plt.show()