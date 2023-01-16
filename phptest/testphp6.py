import requests


datas={
    "ownid": "34347",
    "customerid": "2233",

}
res= requests.post("http://103.47.81.197:8081/findPhoto",json=datas)

print(res.text)