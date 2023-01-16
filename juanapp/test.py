import requests

url="http://182.61.46.244:8880/user/login"
data={
    "uuid":"999908"
}
res=requests.post(url=url,data=data)
print(res.text)


import copy

copy.deepcopy()