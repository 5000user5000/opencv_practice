import cv2
import numpy as np

#RGB都0->黑照片
img = np.zeros((600,600,3),np.uint8) #600*600,channel 3,每一個值8bits(0~255)

#畫線,(原圖,起點,終點,顏色,粗度)
#cv2.line(img,(0,0),(400,300),(200,110,20),2)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(200,110,20),2) #shape[1]寬,[0]是高

#畫方形,左上角->右下角 座標,其餘和line一樣
#cv2.rectangle(img,(0,0),(400,300),(102,153,200),1)
cv2.rectangle(img,(0,0),(400,300),(102,153,200),cv2.FILLED)#填滿

#畫圓,圓心座標,半徑...
cv2.circle(img,(300,400),30,(111,222,5),1)

#寫字  (原圖,文字,座標,字體,粗度,顏色) P.S.這個不能寫中文的
cv2.putText(img,'hello world',(100,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,150),2)

cv2.imshow('img',img)
cv2.waitKey(0)