import os

def ContainStr(filepath,s):
    if(os.path.exists(filepath)):
        with open(filepath,"r")as f:
            lines =f.readlines()
            for line in lines:
                if s in line:
                    return True
                else:
                    return  False
    else:
        "没有该路径文件"



data =ContainStr("123.txt","s")
print(data)