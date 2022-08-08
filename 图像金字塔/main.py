import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("AM.png")
print(img.shape)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
up=cv2.pyrUp(img)
print(up.shape)
# cv2.imshow("up",up)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

down=cv2.pyrDown(img)
print(down.shape)
# cv2.imshow("down",down)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#拉普拉斯金字塔
#down_up=cv2.pyrUP(down)
#x_res=img-down_up


#图像轮廓
#cv2.findContours(img,mode,method)
#
img=cv2.imread("contours.png")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#为了更高的准确率使用二值图像.
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# cv2.imshow("thresh",thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
binary,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#绘制轮廓
#传入绘制图像,轮廓，轮廓索引 颜色模式 线条厚度
# res =cv2.drawContours(img,contours,-1,(0,0,255),2)
# cv2.imshow("res",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


# res =cv2.drawContours(img,contours,0,(0,0,255),2)
# cv2.imshow("res",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
#轮廓特征
#面积
# cnt=contours[0]
# cv2.contourArea(cnt)
# #周长 true表示闭合的
# cv2.arcLength(cnt,True)
#轮廓近似
img=cv2.imread("contours2.png")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
binary,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contours[0]
draw_img =img.copy()
res =cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
# cv2.imshow("res",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
# epsilon =0.1*cv2.arcLength(cnt,True)
# approx =cv2.approxPolyDP(cnt,epsilon,True)
#
# draw_img=img.copy()
# res =cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
# cv2.imshow("res",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#边界矩形
img=cv2.imread("contours.png")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
binary,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contours[0]
x,y,w,h =cv2.boundingRect(cnt)
imgs=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow("imgs",imgs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#area
area=cv2.contourArea(cnt)
x,y,w,h=cv2.boundingRect(cnt)
rect_area=w*h
extent =float(area)/rect_area
print("轮廓面积与边界矩形比",extent)
#外接圆
(x,y),radius=cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius =int(radius)
imgs =cv2.circle(img,center,radius,(0,255,0),2)
# cv2.imshow("imgs",imgs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

##模版匹配
#模版匹配和卷积原理很像，模版在原图像上从原点开始滑动，计算模版与
#图像被模版覆盖的地方的差别程度，这个差别程度的计算方法在opencv里有6种，计算后将每次计算的结果放入到一个矩阵里，作为结果输出，假如
#原图形是A*B大小 则出书结果的矩阵是(A-a+1)(B-b+1)

img=cv2.imread("lena.jpg",0)
template =cv2.imread("face.jpg",0)
h,w=template.shape[:2]
print(img.shape)
print(template.shape)

methods=["cv2.TM_CCOEFF","cv2.TM_CCOEFF_NORMED","cv2.TM_CCORR","cv2.TM_CCORR_NORMED","cv2.TM_SQDIFF","cv2.TM_SQDIFF_NORMED"]
# res =cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
# print(res.shape)
# min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
# print(min_val,max_val,min_loc,max_loc)

# for meth in methods:
#     img2=img.copy()
#     method =eval(meth)
#     res=cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     #如果是平方差匹配TM_SQDIFF或归一化平方差匹配cv2.TM_SQDIFF_NORMED取最小值
#     if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
#         top_left=min_loc
#     else:
#         top_left=max_loc
#     bottom_right =(top_left[0]+w,top_left[1]+h)
#     #画矩形
#     cv2.rectangle(img2,top_left,bottom_right,255,2)
#
#     plt.subplot(121)
#     plt.imshow(res,cmap="gray")
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(img2,cmap="gray")
#     plt.subplot(122)
#     plt.imshow(img2, cmap="gray")
#     plt.xticks([])
#     plt.yticks([])
#     plt.show()

#匹配多个对象
img_rgb =cv2.imread("mario.jpg")
img_gray =cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread("mario_coin.jpg",0)
h,w=template.shape[:2]
res =cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.8
#取大于等于0.8的坐标
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]): #*号表示可选参数
    bottom_right =(pt[0]+w,pt[1]+h)
    cv2.rectangle(img_rgb, pt, bottom_right, (0,0,255), 2)

cv2.imshow("img_rgb",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

