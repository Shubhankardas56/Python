import cv2
cap = cv2.VideoCapture(0)
cap.set(1,640)
cap.set(2,440)
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break