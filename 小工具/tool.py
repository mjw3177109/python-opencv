import tkinter as tk
import os


file_dir="./"
for root, dirs, files in os.walk(file_dir):
    print('root_dir:', root)  #当前路径
    print('sub_dirs:', dirs)   #子文件夹
    print('files:', files)     #文件名称，返回list类

start=0
for f in files:
    filename=f.split(".")[-1]
    if filename =='jpg' or filename=='png' or filename=='jpeg' or filename=='gif':
        os.rename(f, "inspection_"+str(start) + "." + filename)
        start += 1



