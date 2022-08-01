import cv2

def read_picture():
    #照片讀取
    img = cv2.imread('reimu.jpg')
    #img = cv2.resize(img,(300,300)) #改大小
    #img = cv2.resize(img,(0,0),fx=0.5,fy=0.5) #fx是縮放0.5倍(寬),fy高
    cv2.imshow('ing',img)
    cv2.waitKey(1000) #等待鍵盤按鍵,等待1秒圖片就關掉,按下鍵會直接關掉,回傳你按的鍵,0表示無限久
 
def read_video():
    #影片讀取
    cap = cv2.VideoCapture(1)
    
    while True:
        ret , frame = cap.read() #ret是return 縮寫,返回值
        if ret:
            frame = cv2.resize(frame,(0,0),fx=1.2,fy=1.2)
        else:
            break
if __name__ == '__main__':
    read_picture()
    #read_video() #影片就自己找吧  