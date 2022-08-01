from ast import For
import cv2

img = cv2.imread('shape.jpg')
imgCountour = img.copy()#先複製一張,cnt那裏畫圖在上
#先轉灰階,因為輪廓檢測不須顏色
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,150,200)
#開始偵測輪廓,回傳輪廓和階層 , external表示是看外部輪廓,CHAIN_APPROX_NONE是不壓縮的意思
contours , hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#印出輪廓(描邊)
for cnt in contours:
    #print(cnt) #印出輪廓點座標,連在一起就是一個輪廓的樣子
    cv2.drawContours(imgCountour,cnt,-1,(255,0,0),4) #要畫的圖上,座標點,要畫第幾個圖(-1表示全部),顏色,線條粗度
    #print(cv2.contourArea(cnt))#計算每個形狀的面積
    #print(cv2.arcLength(cnt,True))#周長,true表示線條是閉合的
    area = cv2.contourArea(cnt)
    if area > 500: #只看面積>500者(過濾細小雜訊)
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt,peri*0.02,True)#頂點位置,多邊形近似輪廓
        #print(len(vertices))#頂點數
        corner = len(vertices)
        x,y,w,h = cv2.boundingRect(vertices)
        cv2.rectangle(imgCountour,(x,y),(x+w,y+h),(0,255,0),4)#會看到綠色方形把每個圖框起來
        if corner ==3:
            cv2.putText(imgCountour,'triangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        if corner ==4:
            cv2.putText(imgCountour,'rectangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        if corner >6:
            cv2.putText(imgCountour,'circle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgCountour',imgCountour)
cv2.waitKey(0)