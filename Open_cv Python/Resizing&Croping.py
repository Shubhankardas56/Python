import cv2

img = cv2.imread('logo.png')
print(img.shape)
resized=cv2.resize(img,(120,120))

croped=img[0:225,0:120]

cv2.imshow('Output',img)
cv2.imshow('Resized img',resized)
cv2.imshow('croped img',croped)


cv2.waitKey(0)