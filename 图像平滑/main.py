import cv2
import numpy as np
img=cv2.imread('lenaNoise.png')
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
#
# #均值滤波
# #简单的平均卷积操作
#
# blur =cv2.blur(img,(3,3))
# cv2.imshow("blur",blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

##方框滤波
#基本和均值一样
# box=cv2.boxFilter(img,-1,(3,3),normalize=True)
#
# cv2.imshow("box",box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#不归一化 会有溢出255的问题
# box=cv2.boxFilter(img,-1,(3,3),normalize=False)
#
# cv2.imshow("box",box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#高斯滤波
#高斯模糊的卷积核里的树枝是满足高斯分布,相当于更重视中间的值
# aussian=cv2.GaussianBlur(img,(5,5),1)
#
# cv2.imshow("aussian",aussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#中值滤波
#用中值代替均值
median =cv2.medianBlur(img,5)
cv2.imshow("median",median)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


#展示所有
# res =np.hstack((blur,aussion,median))
# cv2.imshow("median vs average",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)