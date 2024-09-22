import cv2
import numpy as np
img=cv2.imread('logo.png')

B,G,R=cv2.split(img)

newimg=np.zeros(img.shape[:2],dtype='uint8')



cv2.imshow('Output',img)
cv2.imshow('red img',cv2.merge([newimg,newimg,R]))
cv2.imshow('green img',cv2.merge([newimg,G,newimg]))
cv2.imshow('blue img',cv2.merge([B,newimg,newimg]))

cv2.waitKey(0)