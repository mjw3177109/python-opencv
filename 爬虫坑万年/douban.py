import requests

import json


if __name__ == '__main__':
    url="https://movie.douban.com/j/chart/top_list"
    word="喜剧"
    params={
       "type_name":word,
        "type":24,
        "interval_id":"100:90",
        "action":"",
        "start":0,
        "limit": 20,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    res=requests.get(url=url,params=params,headers=headers)
    result=res.json()
    print(result)
    fileName=word+".json"
    fp=open(fileName,"w",encoding="utf-8")
    json.dump(result, fp, ensure_ascii=False)
    print("over!!!")
