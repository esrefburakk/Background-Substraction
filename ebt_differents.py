import cv2
import numpy as np

bg = cv2.VideoCapture("background.mp4")
cap = cv2.VideoCapture("video2.mp4")

ret1,frame1 = bg.read()

frame1 = cv2.resize(frame1,(640,480))
frame1 = cv2.GaussianBlur(frame1,(5,5),0)

gray_frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray_frame1 = cv2.GaussianBlur(gray_frame1,(5,5),0)

while True:
    ret2,frame2 = cap.read()
    if frame2 is None:
        break

    frame2 = cv2.resize(frame2,(640,480))
    frame2 = cv2.GaussianBlur(frame2,(5,5),0)

    gray_frame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    gray_frame2 = cv2.GaussianBlur(gray_frame2,(5,5),0)

    diff1 = gray_frame1 - gray_frame2
    diff2 = gray_frame2 - gray_frame1

    diff3 = cv2.absdiff(gray_frame1,gray_frame2)
    diff4 = cv2.absdiff(gray_frame2,gray_frame1) 

    _,diff1 = cv2.threshold(diff1,35,225,cv2.THRESH_BINARY)
    _,diff2 = cv2.threshold(diff2,35,225,cv2.THRESH_BINARY)
    _,diff3 = cv2.threshold(diff3,35,225,cv2.THRESH_BINARY)
    _,diff4 = cv2.threshold(diff4,35,225,cv2.THRESH_BINARY)  

    cv2.imshow("Difference1",diff1)
    cv2.imshow("Difference2",diff2)
    cv2.imshow("Difference3",diff3)
    cv2.imshow("Difference4",diff4) 

    if cv2.waitKey(1) == 27:
        break


bg.release()
cap.release()
cv2.destroyAllWindows()
