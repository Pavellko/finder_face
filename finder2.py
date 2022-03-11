import cv2
import os

x = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

img = cv2.imread('001.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
det = x.detectMultiScale(img, 1.1, 19)
for (x,y,w,h) in det:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=3)

cv2.imshow('Result', img)
cv2.waitKey(0)

