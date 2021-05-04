# Resizing & Rescaling
import cv2 as cv

# 비디오와 이미지 사이즈 조정 함수 Every Images, Videos, and Live Video 에 적용가능
def rescaleFrame(frame, scale=0.75): # By default, 0.75
    width = int(frame.shape[1] * scale) # width of your image
    height = int(frame.shape[0] * scale) # height of your image
    dimensions = (width, height) # 튜플

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# 비디오 해상도 조정 함수 Only works for Live Video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
    

## Reading Images & 사이즈 조정
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img, 0.2)
cv.imshow('Resized Cat', resized_image)
cv.waitKey(0)

## Reading Videos & 사이즈 조정
capture = cv.VideoCapture('Videos/dog.mp4') # VideoCapture(0) references my webcam
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2) # 기본 값을 0.75 로 설정해두었지만, 여기서 변경 가능

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized) 


    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
