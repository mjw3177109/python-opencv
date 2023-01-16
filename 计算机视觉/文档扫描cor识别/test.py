import pytesseract
from PIL import Image

img = Image.open('scan.jpg')
num = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
print(num)	# 输出图片识别后的字符串
