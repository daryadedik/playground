#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('/home/darya/Downloads/opencv_250w.png')
pixel = image[100,100]

#accessing and modifying pixels
image.item(10,10,2) #red value of pixel (10,10); B(0),G(1),R(2) - channels
#image.itemset((10,10,2), 200)

#image shape
image.shape

#total num of pixels
image.size

#image datatype
image.dtype

#select area of image
#patch = image[300:350, 330:380]
#image[550:600, 100:150] = patch

#split into RGB
#b,g,r = cv2.split(image)
#merge
#image = cv2.merge((b,g,r))
#to change red pixels to 0
#image[:,:,2] = 0

#cv2.imshow('image',image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#BLUE = [255,0,0]
#replicate = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
#reflect = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
#reflect101 = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT_101)
#wrap = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
#constant= cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE) 

#plt.subplot(231),
plt.imshow(image,'gray'),plt.title('ORIGINAL')
#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
#plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
#plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
#plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
#plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
