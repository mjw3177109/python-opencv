import requests


datas={
    "ownid": "34347",

}
res= requests.post("http://103.47.81.197:8081/searchPhoto",json=datas)

print(res.text)