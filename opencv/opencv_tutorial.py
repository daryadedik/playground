#!/usr/bin/env python

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/darya/Downloads/noguchi02.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

average_color_per_row = np.average(img, axis=0) 
average_color = np.average(average_color_per_row, axis=0)
average_color = np.uint8(average_color)
average_color_img = np.array([[average_color]*100]*100, np.uint8)
plt.imshow(average_color_img)
#plt.imshow(img[:,:,1], "spectral")
plt.show()

average_col = np.array([np.average(img, axis=1)]*500, np.uint8)
plt.subplot(211)
plt.imshow(average_col)

average_row = np.array([np.average(img, axis=0)]*500, np.uint8)
plt.subplot(212)
plt.imshow(average_row)
plt.show()






