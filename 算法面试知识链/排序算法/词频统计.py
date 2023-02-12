#词频统计:输入字符串,词和词之间空格隔开,输出单词和词频,按照词频大小从大到小顺序输出

def countStrNumber(datas):
    if len(datas)<=0:
        return
    newdata=datas.replace(" ","")
    print(newdata)
    dicts ={}
    for s in newdata:
        number=newdata.count(s)
        dicts[s]=number
    newdatas=sorted(dicts.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(newdatas)-1):
        print(newdatas[i])

countStrNumber("0 2 3 2 9 3 0 2 9 3 9 4 9 8 9 s s s s 8 d 7 8 d s ")