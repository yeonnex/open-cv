import cv2 as cv

img = cv.imread("Photos/group 1.jpg")
cv.imshow("Group people", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y), (x+w, y+w),(0,255,0),thickness =2)
cv.imshow('Detected faces', img)

# haar cascade are really sensitive to noise 
cv.waitKey(0)