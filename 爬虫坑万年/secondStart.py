import requests

#UA检测: 门户网站的服务器会检测对应请求的载体身份标识,如果检测到请求的载体身份标识为某一浏览器,
# 说明该请求是一个正常请求(用户向浏览器发送的请求)如果检测到请求的载体身份标识不是基于某一款浏览器
#则表示该请求不是一个正常请求,则服务器很有可能拒绝该请求
#UA User-Agent{} 请求载体的身份标识
#UA伪装 让爬虫对应的请求载体身份标识伪装成某一款浏览器就可以了
if __name__ =="__main__":
    url ="https://www.sogou.com/web"
    kw="装逼"
    params={
        "query":kw
    }
    #将对应的user-agent封装到一个字典中
    headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    res=requests.get(url,params=params,headers=headers)
    print(res.text)
    fileName=kw+".html"
    with open(fileName,"w",encoding="utf-8") as f:
        f.write(res.text)
    print(fileName,'保存成功!!!')