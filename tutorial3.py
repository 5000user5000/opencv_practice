import cv2
import numpy as np


img = cv2.imread('reimu.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

#轉成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#(高斯)模糊
blur = cv2.GaussianBlur(img,(71,71),50) #kernel不行用偶數,只能用奇數 標準差0
#取得邊緣 ,數字越大越簡略
canny = cv2.Canny(img,150,250)
#膨脹,線條變粗
kernel = np.ones((3,3),np.uint8)
dilate = cv2.dilate(canny,kernel,iterations=1) #膨脹次數
#侵蝕,線條變細
erode = cv2.erode(dilate,kernel,iterations=1)


cv2.imshow('img',img) #(小視窗標題,引入的圖片)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)

#有空可以去研究背後的數學原理