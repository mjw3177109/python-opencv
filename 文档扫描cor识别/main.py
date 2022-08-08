import numpy as np
import argparse
from utils.decoractor import timing
import cv2
from  utils.tools import resize,order_points,four_point_transform
from PIL import Image
import pytesseract
import os
image_path ="images/receipt.jpg"

#读取输入
image =cv2.imread(image_path)
#坐标也会相同变化
ratio=image.shape[0]/500.0
orig =image.copy()

image =resize(orig,height=500)
#预处理
gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray =cv2.GaussianBlur(gray,(5,5),0)
edged =cv2.Canny(gray,75,200)
#展示预处理结果
print("STEP 1: 边缘检测")
#cv2.imshow("Image", image)
# cv2.imshow("Edged", edged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 轮廓检测
cnts =cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
cnts =sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
#遍历轮廓
for c in cnts:
    # 计算轮廓近似
    peri =cv2.arcLength(c,True)
    # C表示输入的点集
    #epsion表示从原始轮廓到近似轮廓的最大距离，它是一个准确度参数
    #True表示封闭的
    approx =cv2.approxPolyDP(c,0.02*peri,True)
    # 4个点的时候就拿出来
    if len(approx) ==4:
        screenCnt =approx
        break


#展示结果
print("STEP 2 :获取轮廓")
cv2.drawContours(image,[screenCnt],-1,(0,255,0),2)
# cv2.imshow("Outline",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 透视变换
warped =four_point_transform(orig,screenCnt.reshape(4,2)*ratio)
#二值处理
warped =cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
ref =cv2.threshold(warped,100,255,cv2.THRESH_BINARY)[1]
cv2.imwrite('scan.jpg',ref)
#展示结果
print("STEP 3:变换")
#cv2.imshow("Original", resize(orig, height = 650))
# cv2.imshow("Scanned", resize(ref, height = 650))
# cv2.waitKey(0)
preprocess = 'blur'  # thresh

image = cv2.imread('scan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

if preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)


text = pytesseract.image_to_string(Image.open('scan.jpg'))
print(text)
os.remove('scan.jpg')

cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)