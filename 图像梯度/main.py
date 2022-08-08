#图像梯度-Sobei算子

import cv2
import numpy as np
#dst=cv2.Sobei(src,ddepth,dx,dy,ksize)
#ddepth:图像的深度
#dx和dy分别代表水平和竖直方向
#ksize是Sobei算子的大小

img =cv2.imread("pie.png",cv2.IMREAD_GRAYSCALE)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

soblex=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# cv2.imshow("soblex",soblex)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#白到黑是正数  黑到白是负数, 所有的负数都会截断成0，所以要取绝对值
soblexx=cv2.convertScaleAbs(soblex)
# cv2.imshow("soblexx",soblexx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

sobley=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobleyy=cv2.convertScaleAbs(sobley)
# cv2.imshow("sobleyy",sobleyy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
sobelxy =cv2.addWeighted(soblexx,0.5,sobleyy,0.5,0)
# cv2.imshow("sobelxy",sobelxy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#不建议直接计算
# sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
# newsobleyy=cv2.convertScaleAbs(sobelxy)

###图像梯度-Scharr算子
#scharrx=cv2.Scharr(img,cv2.CV_64F,1,0,ksize=3)
#cv2.convertScaleAbs(scharrx)
##图像梯度-laplacian算子
# laplacian =cv2.Laplacian(img,cv2.CV_64F)
#cv2.convertScaleAbs(laplacian)

##Canny边缘检测算法
#1.使用高斯滤波器,以平滑图像,滤除噪声
#2.计算图像中美观像素点的梯度强度和方向
#3.应用非极大值(Non-Maximum Supperession) 抑制,以消除边缘检测带来的杂散响应。
#4.应用双阈值(Double-Threshold)检测来确定真实和潜在的边缘。
#5.通过抑制孤立的弱边缘最终完成边缘检测

#1。高斯滤波器

img =cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
v1=cv2.Canny(img,80,150)
#越小边界越大
v2=cv2.Canny(v1,50,100)
#
res =np.hstack((v1,v2))
cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
