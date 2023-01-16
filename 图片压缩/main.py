from PIL import Image
import os

#获取文件夹里面的图片

path="./cat.jpg"
im = Image.open(path)
(x, y) = im.size  # 读取图片尺寸（像素）
x_1 = 500  # 定义缩小后的标准宽度
y_1 = int(y * x_1 / x)  # 计算缩小后的高度
out = im.resize((x_1, y_1), Image.ANTIALIAS)  # 改变尺寸，保持图片高品质
out.save('./new/{}'.format(path.split("\\")[-1]))
