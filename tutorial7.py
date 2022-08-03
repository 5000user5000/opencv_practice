import cv2
img = cv2.imread('meme.jpg')

#轉灰階,因為不需要是彩色
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#載入人臉辨識模型
faceCascade = cv2.CascadeClassifier('face_detect.xml')

faceRect = faceCascade.detectMultiScale(gray,1.1,3)#辨識用圖,縮放倍數(多次縮小+偵測)(值越小,縮小倍數越大,要跑越久)//或是指偵測視野放大,偵測的視野,這張圖的臉至少要被框到幾次才會被認定

#先確認有看到幾張臉
print(len(faceRect))

for (x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
cv2.imshow('img',img)
cv2.waitKey(0)

#到https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml 下載或貼到自己的xml檔