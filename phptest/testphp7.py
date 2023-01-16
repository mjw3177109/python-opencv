import requests


datas={
    "ownid":"213",
    "customerid":"8887878",
    "file":"flienew",

}

res= requests.post("http://103.47.81.197:8081/postPhoto",json=datas)

print(res.text)