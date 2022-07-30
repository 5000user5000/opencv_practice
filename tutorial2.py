import cv2
import numpy as np
import random

def imageInfo():
    img = cv2.imread('reimu.jpg')
    print(type(img)) #numpy arr
    print(img.shape) # (676, 850, 3) = (寬,高,RGB3色)
    '''
    (676, 850, 3) 陣列表示
    3個值 B G R 的量
    [
    
        [ [3個值],[255,5,185],[],...850     ],
        [[],[],[],...850     ],
        [[],[],[],...850     ],
        ...676
    ]
    '''
def make_image():
    #img = np.empty((300,300,3),np.uint8) # unit8 -> 8bit,u 正整數 創造空陣列
    img = cv2.imread('reimu.jpg') #引入照片,把小部分改掉
    #填滿
    for row in range(300):
        for col in range(300):
            #img[row][col] = [15,160,255] #自己可調看看這3個值
            img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]#都隨機給,看起來像雜訊
    cv2.imshow('img',img)
    cv2.waitKey(2000)
    #擷取圖片
    newImg = img[:150,200:400] #圖片擷取寬0~150 ,高200~400
    cv2.imshow('new_img',newImg)
    cv2.waitKey(2000)

if __name__ == '__main__':
    #imageInfo() #顯示圖片資料
    make_image()

