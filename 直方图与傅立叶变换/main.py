import numpy as np

import matplotlib.pyplot as plt

import cv2



#cv2.calcHist(images,channels,mask,histSize,ranges)

#images 原图像图像格式为unit8或float32,当传入函数时应用中括号【】来例如[img]
#channels,同样用中括号来它回告诉函数我们统计图像的的直方图，如果输入图像是灰度 它的值就是【0】，如果是彩色图像可以是[0][1][2]它们对应BGR
#mask 掩摸图像，统计整幅图像的直方图就把它设为None，但是如果你想说图像某一方面的直方图你就制作一个掩模图像并使用它
#histSize:bin的数目，也用中括号来
#ranges 像素值范围为【0-256】
#img=cv2.imread("cat.jpg",0) #0表示灰度图
# hist=cv2.calcHist([img],[0],None,[256],[0,256])
# print(hist.shape)
#
# plt.hist(img.ravel(),256)
# plt.show()
img=cv2.imread("cat.jpg")
# color=("b","g","r")
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img], [i], None, [256], [0,256])
#     plt.plot(histr,color=col)
#     plt.xlim(0,256)
# plt.show()

#mask操作
#创建mask

mask=np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400]=255
# cv2.imshow("mask",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

imgs=cv2.imread("clahe.jpg",0)
#mask_img=cv2.bitwise_and(imgs,imgs,mask=mask)
#
# cv2.imshow("mask_img",mask_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

# hist_full=cv2.calcHist([imgs], [0], None, [256], [0,256])
#
# hist_mask=cv2.calcHist([imgs], [0], mask, [256], [0,256])
#
# plt.subplot(221)
# plt.imshow(img,cmap="gray")
# plt.subplot(222)
# plt.imshow(mask,cmap="gray")
# plt.subplot(223)
# plt.imshow(mask_img,cmap="gray")
# plt.subplot(224)
# plt.plot(hist_full)
# plt.plot(hist_mask)
# plt.xlim(0,256)
# plt.show()

#直方图均衡化
# plt.hist(imgs.ravel(),256)
# # plt.show()
#
equ=cv2.equalizeHist(imgs)
# plt.hist(equ.ravel(),256)
# plt.show()

#自适应直方图均衡化
clahe =cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
# res_clahe=clahe.apply(imgs)
# res=np.hstack((imgs,equ,res_clahe))
# cv2.imshow("res",res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

#傅立叶变换

#傅立叶变换的作用
#高频:变化剧烈的灰度分量，例如边界
#低频：变化缓慢的灰度分量，例如一片大海
#滤波
#低通道滤波：只保留低频，会使得图像模糊
#高通道滤波器：只保留高频，会使得图像细节增强
#opencv中主要就是cv2.dft和cv2.idft(),输入图像需要先转换成np.float32格式
#得到的结果中频率为0的那部分会在左上角，通常要转换到中心位置可以通过
#shift变换来实现。
#cv2.dft()返回的结果是双通道的(实部，虚部) 通常还需要转化成图像格式才能展示(0,255).
imgs=cv2.imread("lena.jpg",0)

img_float32=np.float32(imgs)

dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
#得到灰度图能表示的形式
# magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# plt.subplot(121)
# plt.imshow(imgs,cmap="gray")
# plt.title("Input Image")
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(magnitude_spectrum,cmap="gray")
# plt.title("Magnitude_Spectrum")
# plt.xticks([])
# plt.yticks([])
# plt.show()

#低通滤波
rows,cols=imgs.shape
crow,ccol=int(rows/2),int(cols/2) #中心位置

# mask=np.zeros((rows,cols,2),np.uint8)
# mask[crow-30:crow+30,ccol-30:ccol+30]=1
#高通
mask=np.ones((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30]=0


#IDFT
fshift=dft_shift*mask
f_ishift =np.fft.fftshift(fshift)
img_back=cv2.idft(f_ishift)
img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121)
plt.imshow(imgs,cmap="gray")
plt.title("Input Image")
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(img_back,cmap="gray")
plt.title("result")
plt.xticks([])
plt.yticks([])
plt.show()