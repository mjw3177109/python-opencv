import numpy as np
import argparse
from utils.decoractor import timing
import cv2
from  utils.tools import sort_contours,resize

# ap=argparse.ArgumentParser()
# ap.add_argument("-i","--image",required=True,help="path to input image")
# ap.add_argument("-t","--template",required=True,help="path to template OCR A image")
#
# args =vars(ap.parse_args())

FIRST_NUMBER={
    "3":"American Express",
    "4":"Visa",
    "5":"MasterCard",
    "6":"Discover Card",
}

template_path ="./images/ocr_a_reference.png"
image_path ="./images/credit_card_01.png"
#读取模版
img =cv2.imread(template_path)
#为得到轮廓 转灰度图
ref =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#转为二值图像,因为检测轮廓进来的数值都是二值图
ref =cv2.threshold(ref,10,255,cv2.THRESH_BINARY_INV)[1]

#计算轮廓
#cv2.RETR_EXTERNAL 只检测外轮廓,cv2.CHAIN_APPROX_SIMPLE只检测终点的坐标
ref_,refCnts,hierarchy =cv2.findContours(ref.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#在原图上画出
cv2.drawContours(img,refCnts,-1,(0,0,255),3)

#打印轮廓个数
#print(np.array(refCnts).shape)

#
refCnts=sort_contours(refCnts,method="left-to-right")[0]

digits={
}

for(i,c) in enumerate(refCnts):
    (x,y,w,h) =cv2.boundingRect(c)
    roi=ref[y:y+h,x:x+w]
    roi=cv2.resize(roi,(57,88))

    digits[i]=roi

##初始化卷积核
rectKernel =cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
sqKernel =cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
#读取进来的信用卡图片
image =cv2.imread(image_path)
image =resize(image,width=300)
gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("img", gray)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

#礼帽操作，突出更明亮的部分
tophat =cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,rectKernel)
# cv2.imshow("tophat", tophat)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, #ksize=-1相当于用3*3的
	ksize=-1)


gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
gradX = gradX.astype("uint8")
print(np.array(gradX).shape)
# cv2.imshow("gradX", gradX)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
#通过闭操作（先膨胀，再腐蚀）将数字连在一起
gradX=cv2.morphologyEx(gradX,cv2.MORPH_CLOSE,rectKernel)
# cv2.imshow("gradX", gradX)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
#THRESH_OTSU会自动寻找合适的阈值，适合双峰，需把阈值参数设置为0
thresh = cv2.threshold(gradX, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow("gradX", thresh)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
#再来一个闭操作

thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel) #再来一个闭操作
# cv2.imshow("thresh", thresh)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

thresh_,threshCnts,hierarchy =cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts =threshCnts
cur_img=image.copy()
cv2.drawContours(cur_img,cnts,-1,(0,0,255),3)
# cv2.imshow("img", cur_img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
locs=[]
#遍历轮廓
for (i,c) in enumerate(cnts):
    # 计算矩形
    (x,y,w,h) =cv2.boundingRect(c)
    ar =w/float(h)

    # 选择合适的区域，根据实际任务来，这里的基本都是四个数字一组
    if ar > 2.5 and ar < 4.0:

        if (w > 40 and w < 55) and (h > 10 and h < 20):
            # 符合的留下来
            locs.append((x, y, w, h))
#将符合的轮廓从左到右排序
locs =sorted(locs,key =lambda x:x[0])
output=[]

#遍历每一个轮廓中的数字
for (i,(gX,gY,gW,gH)) in enumerate(locs):
    # initialize the list of group digits
    groupOutput =[]

    #根据坐标提取每一个组
    group =gray[gY-5:gY+gH+5,gX-5:gX+gW+5]
    # cv2.imshow("group", group)
    # cv2.waitKey(0)
    # cv2.destoryAllWindows()
    #break
    #预处理
    group =cv2.threshold(group,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    # cv2.imshow("group", group)
    # cv2.waitKey(0)
    # cv2.destoryAllWindows()
    # break
    # 计算每一组的轮廓
    group_,digitCnts,hierarchy =cv2.findContours(group.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    digitCnts =sort_contours(digitCnts,method="left-to-right")[0]

    #计算每一组中的每一个数值
    for c in digitCnts:
        # 找到当前数值的轮廓，resize成合适的的大小
        (x, y, w, h) = cv2.boundingRect(c)
        roi = group[y:y + h, x:x + w]
        roi = cv2.resize(roi, (57, 88))
        # cv2.imshow("roi", roi)
        # cv2.waitKey(0)
        # cv2.destoryAllWindows()

        #计算匹配得分
        scores =[]

        #在模版中计算每一个得分
        for (digit ,digitROI) in digits.items():
            # 模板匹配
            result =cv2.matchTemplate(roi,digitROI,cv2.TM_CCOEFF)
            (_,score,_,_)=cv2.minMaxLoc(result)
            scores.append(score)

        #得到最合适的数字
        groupOutput.append(str(np.argmax(scores)))
    #画出来
    cv2.rectangle(image,(gX-5,gY-5),(gX+gW+5,gY+gH+5),(0,0,255),1)
    cv2.putText(image,"".join(groupOutput),(gX,gY-15),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,255),2)


    #得到结果
    output.extend(groupOutput)
        # break
    # break


#打印结果
print("Credit Card Type:{}",format(FIRST_NUMBER[output[0]]))
print("Credit Card #:{}".format("".join(output)))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destoryAllWindows()
