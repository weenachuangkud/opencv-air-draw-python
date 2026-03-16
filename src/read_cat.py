import cv2

img = cv2.imread('Photos/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)