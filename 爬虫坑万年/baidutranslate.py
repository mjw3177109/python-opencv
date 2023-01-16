#需求破解百度翻译 post请求(携带了参数)
#响应数据是一个json数据
import json
import requests
if __name__=="__main__":
    post_url="https://fanyi.baidu.com/sug"
    #post请求参数处理(同get请求一致)
    word="dog"
    data={
        "kw":word
    }
    #进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    response =requests.post(url=post_url,headers=headers,data=data)
    #5.获取响应数据:json()方法返回的是obj(如果确认响应数据是json类型的,才可以使用json())
    res=response.json()
    #持久化存储
    fp=open(word+".json","w",encoding="utf-8")
    json.dump(res,fp,ensure_ascii=False)
    print("over!!!")















    print(response.text)