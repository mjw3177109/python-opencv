import cv2
import numpy as np

# img =cv2.imread("dige.png")
#
# kernel =np.ones((5,5),np.uint8)
# erosion =cv2.erode(img,kernel,iterations=1)
# cv2.imshow("erosion",erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

# res =np.hstack((img))
# cv2.imshow("all images",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


# pie =cv2.imread("pie.png")
#
# kernel =np.ones((30,30),np.uint8)
# erosion_1=cv2.erode(pie,kernel,iterations=1)
# erosion_2=cv2.erode(pie,kernel,iterations=2)
# erosion_3=cv2.erode(pie,kernel,iterations=3)
# res =np.hstack((erosion_1,erosion_2,erosion_3))
# cv2.imshow("all images",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

####形态学 膨胀
# img =cv2.imread("dige.png")
#
# kernel =np.ones((3,3),np.uint8)
# dige_erosion =cv2.erode(img,kernel,iterations=1)
# kernel =np.ones((3,3),np.uint8)
# dige_dilate=cv2.dilate(dige_erosion,kernel,iterations=1)
#
# cv2.imshow("erosion",dige_dilate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#开运算和闭运算
#开先腐蚀后膨胀
# img =cv2.imread("dige.png")
# kernel =np.ones((5,5),np.uint8)
# opening =cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# cv2.imshow("opening",opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#闭 先膨胀再腐蚀
# img =cv2.imread("dige.png")
# kernel =np.ones((5,5),np.uint8)
# closing =cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# cv2.imshow("closing",closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#梯度运算
#梯度=膨胀-腐蚀
# pie =cv2.imread("pie.png")
#
# kernel =np.ones((7,7),np.uint8)
# dilate=cv2.dilate(pie,kernel,iterations=5)
# erosion =cv2.erode(pie,kernel,iterations=5)
# res=np.hstack((dilate,erosion))
# # cv2.imshow("res",res)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # cv2.waitKey(1)
# gradient=cv2.morphologyEx(pie,cv2.MORPH_GRADIENT,kernel)
# cv2.imshow("gradient",gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#礼帽与黑帽
#礼帽=原始输入-开运算结果
#黑帽=闭运算-原始输入

#礼帽
img =cv2.imread("dige.png")
kernel =np.ones((5,5),np.uint8)
tophat =cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("tophat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
#黑帽
img =cv2.imread("dige.png")
kernel =np.ones((5,5),np.uint8)
blackhat =cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("blackhat",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)