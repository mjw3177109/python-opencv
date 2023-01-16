import  requests





if __name__=="__main__":
    url="https://www.sogou.com/"
    #setp2 发起请求
    #get方法回返回一个响应对象
    res=requests.get(url=url)
    #step3获取响应数据,text返回的是字符串的响应数据
    print(res.text)
    #step4持久化存储
    with open("./sogou.html","w",encoding="utf-8")as f:
        f.write(res.text)
    print("爬取数据结束")