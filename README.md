https://www.youtube.com/watch?v=oXlwWbU8l2o&t=41s

## OpenCV Course - Full Tutorial with Python

유튜브 **freeCodeCamp.org**의 **OpenCV Course - Full Tutorial with Python**( 약 3시간 40분 소요)를 듣고 공부한 것을 정리하였습니다.

### WHAT I LEARNED

Basics:

- Reading Images and Video
- Image Transformations
- Drawing Shapes
- Putting Texts

Advanced:

- Switching between color Spaces
- BITWISE operations
- Masking
- Histogram Computation
- Edge Detection

Faces:

- Face Detection

- Face Recognition

- Deep Computer Vision (classify between the chracters in the Simpsons)

  ![image-20210504092608889](C:\Users\syhon\AppData\Roaming\Typora\typora-user-images\image-20210504092608889.png)

## Installation

$ pip install opencv-contrib-python

opencv-python 모듈과 opencv-contrib-python 모듈 설치의 차이점은, 후자의 경우 파이썬에서 제공하는 기본 모듈 뿐만 아니라 contribution 모듈도 함께 설치한다는 뜻임

$ pip install caer

Caer is a *lightweight, high-performance* Vision library for high-performance AI research. giving you the **flexibility** to quickly prototype deep learning models and research ideas

## Reading Videos

```python
## Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4') # VideoCapture(0) references my webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

```

cv.waitKey(20) 반드시 필요하다. 얼마의 시간동안 프레임 하나를 보여줄 것인가를 결정한다. 숫자가 커지면 커질수록 하나의 프레임을 보여주는 시간이 길어진다. 위 코드의 경우, 키보드 d 를 누르면 프로그램이 종료된다.

## Resize & Rescale images and videos

계산의 낭비를 막기위해, 일반적으로 이미지의 크기 재조정이 필요하다. 크기가 큰 이미지와 비디오의 경우 정보들이 많이 들어있기에 크기를 조정할 필요가 있다. 크기 줄인다는 의미는 당연히 정보들을 get rid of 하게 된다.

> note! imshow 에서 첫번째 인자인 창의 이름이 같다면 내용물이 다르더라도 첫번째 것만 나오고 똑같은 이름인 밑의 것은 나오지 않으니, 이름은 항상 다른 것으로 지정해주어야한다.

> 또한, 파이썬에서 R,G,B 지정시, (B,G,R)의 순서로 지정해야 한다.

## Color Spaces
openCV에서는 이미지를 BGR 로 나타낸다. 하지만, 다른 데서는 모두 RGB 를 사용하기 때문에 만약 openCV의 imshow 가 아닌 파이플롯의 imshow 로 이미지를 나타내려 할 경우, 채널이 바뀌어서 나타나게된다.

![](2021-05-06-16-47-05.png)
왼쪽의 openCV의 이미지는 BGR 이미지이고, 오른쪽의 경우 RGB 로 그림을 표현하려 했기 떄문에 발생하는 문제이다.

그렇기에 여러 라이브러리들을 사용할 때 컬러스페이스에 대해 항상 생각해주어야한다!!!

## bit-wise operation
openCV에서 비트 연산으로 마스킹을 할 수 있다.

## HOW TO DETECT FACES IN OPENCV with Harr Cascades



