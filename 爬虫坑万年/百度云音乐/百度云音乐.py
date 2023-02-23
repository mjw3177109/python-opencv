import requests
from lxml import etree

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
base_url = "https://music.163.com/discover/artist/cat?id=1001"

response = requests.get(url=base_url, headers=headers)
html = response.content.decode("utf-8")
print(html)