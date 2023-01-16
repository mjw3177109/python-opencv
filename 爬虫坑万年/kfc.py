#http://www.kfc.com.cn/kfccda/index.aspx

import requests
import json

if __name__ == '__main__':
    url ="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
    #将对应的user-agent封装到一个字典中
    headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    kw="深圳"
    data={
        "op":"keyword",
        "cname":"",
        "pid":"",
        "keyword": kw,
        "pageIndex": 1,
        "pageSize": 10,
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    res=requests.post(url,data=data,headers=headers)
    result=res.json()
    print(result)
    fileName=kw+".json"
    fp=open(fileName,"w",encoding="utf-8")
    json.dump(result, fp, ensure_ascii=False)
    print("over!!!")
