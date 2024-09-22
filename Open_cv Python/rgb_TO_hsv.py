import cv2

img=cv2.imread('lena.jpg')
imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)


cv2.imshow('Output',img)
cv2.imshow('HSV IMG',imgHSV)
cv2.imshow('Hue point',imgHSV[:,:,0])
cv2.imshow('Sat point',imgHSV[:,:,1])
cv2.imshow('Val point',imgHSV[:,:,2]) 

 
cv2.waitKey(0)