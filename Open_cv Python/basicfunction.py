import cv2
import numpy as np
# read original image
kernel=np.ones((5,5),np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Original img',img)

# creating the gray image
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray img',grayimg)

# creating binary image
ret, Binaryimg = cv2.threshold(grayimg,125,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Img',Binaryimg)

img1=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('cnv',img1)

img2=cv2.cvtColor(img1,cv2.COLOR_HSV2BGR)
cv2.imshow('cnv2',img2)

img3=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('cnv3',img3)

imgCanny=cv2.Canny(img,120,120)
cv2.imshow('cnv4',imgCanny)

imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow('cnv5',imgDilation)

imgErode=cv2.erode(img,kernel,iterations=1)
cv2.imshow('Erode img',imgErode)

imgErode1=cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow('Erode img1',imgErode1)



cv2.waitKey(0)