# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zz2XRlDrTOKL3zE-lcmZ5bd_v_PJHOaJ
"""

!pip install opencv-python

import cv2
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

cap= cv2.imread('/content/drive/MyDrive/蘇品甄_10611017.jpg')
#img = np.zeros((300,300,3),np.uint8)

cap = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(cap,cv2.COLOR_RGB2HSV)
canny = cv2.Canny(cap,50,100)

plt.imshow(cap)
plt.show()
plt.imshow(canny)

layer =np.empty((cap.shape[0],cap.shape[1],3))

for row in range (cap.shape[0]):
  for col in range(cap.shape[1]):
    layer[row][col] = (255,255,255)

plt.imshow(layer)
plt.show()