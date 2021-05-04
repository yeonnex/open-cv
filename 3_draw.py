import cv2 as cv
import numpy as np

# zeros(): 배열 요소가 모두 0으로 초기화된 Matrix 행렬 생성
blank = np.zeros((500,500,3),dtype='uint8')
print(blank)

cv.imshow('Blank', blank)

print(blank)
# 1. Paint the image a certain color

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green Partially', blank)

blank[:] = 0,255,0
# print(blank)
print(blank[1])
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank,(0,0),(250,500), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)
cv.waitKey(0)



