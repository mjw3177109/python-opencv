import requests



res= requests.get("http://182.61.46.244:8880/category/list")

print(res.json())