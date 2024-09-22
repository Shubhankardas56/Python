import cv2

img = cv2.imread("logo.png")

cv2.imshow("Output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
