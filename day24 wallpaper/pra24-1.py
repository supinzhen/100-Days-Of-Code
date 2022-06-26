#!/usr/bin/env python
# coding: utf-8

# In[106]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[107]:


img = cv2.imread('D:/joker xue/8.jpg')
fImg = img.astype(np.float32)
fImg = fImg / 255.0


# In[108]:


HLS_img = cv2.cvtColor(fImg,cv2.COLOR_BGR2HLS)


# In[109]:


light = -10
HLS_img[:,:,1] = HLS_img[:,:,1] * (light/100.0 + 1)
HLS_img[:,:,1][HLS_img[:,:,1]>1] = 1
result = cv2.cvtColor(HLS_img,cv2.COLOR_HLS2RGB)
result = ((result * 255).astype(np.uint8))


# In[110]:


plt.imshow(result)
plt.show()


# In[133]:


img2 = cv2.imread('D:/joker xue/4.jpg')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HLS)
fimg2 = img2.astype(np.float32)
fimg2 = fimg2/255.0
sat = -50
fimg2[:,:,2] = (sat/100.0+1)*fimg2[:,:,2]
fimg2[:,:,2][fimg2[:,:,2]>1] = 1
result2 = ((fimg2*255).astype(np.uint8))
result2 = cv2.cvtColor(result2,cv2.COLOR_HLS2RGB)
plt.imshow(result2)
plt.show()


# In[ ]:





# In[ ]:




