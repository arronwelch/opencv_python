#!/bin/env python3
# sudo pip install opencv-python
# wget https://github.com/hibyby/GrandmaCan_python_opencv/blob/main/colorcolor.jpg?raw=true
# mv colorcolor.jpg\?raw=true colorcolor.jpg

import cv2

img = cv2.imread("colorcolor.jpg")

#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.resize(img, (0,0), fx=2, fy=2)

cv2.imshow('output', img)

cv2.waitKey(1000) # wait for 1000 ms
#cv2.waitKey(0) # type Ctrl+\ in terminal or anykey in newWindow to close
