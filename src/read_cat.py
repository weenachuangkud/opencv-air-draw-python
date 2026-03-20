import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur cat', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cv.waitKey(0)
