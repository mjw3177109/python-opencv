import requests


datas={
    "ownid":"213",
    "customerid":"8887878",

}

res= requests.post("http://103.47.81.197:8081/uploadTest",json=datas)

print(res.text)