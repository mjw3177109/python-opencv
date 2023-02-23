import requests
from bs4 import BeautifulSoup


host = '110.41.18.114'
import pymongo

client = pymongo.MongoClient(host=host, port=27017, username='admin', password='343340864aA')
# 连接数据库
db = client.admin
emp =db.huilv_data
# # print(db.list_collection_names())  # 获取数据库中所有集合名称
#
import datetime


url="http://fx.cmbchina.com/Hq/"

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
}
res =requests.get(url,headers=headers)
result =[]
if res.status_code ==200:
    soup = BeautifulSoup(res.content , "html.parser")
    datas =soup.find('div', id="realRateInfo").findChildren("tr")
    for tr in datas:
        newdata=tr.find_all('td')
        name =newdata[0].get_text().strip()
        danwei =newdata[1].get_text().strip()
        jibenbi=newdata[2].get_text().strip()
        xianhuisell=newdata[3].get_text().strip()
        monenysell =newdata[4].get_text().strip()
        xianhubuy = newdata[5].get_text().strip()
        monenybuy = newdata[6].get_text().strip()
        time =newdata[7].get_text().strip()
        finalltime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if name!="交易币":
            datas={
                "NameofCurrency":name,
                "TransactionCurrencyUnit":danwei,
                "BaseCurrency":jibenbi,
                "spotSellingPrice": xianhuisell,
                "cashSellingPrice": monenysell,
                "spotBuyingPrice":xianhubuy,
                "cashBuyingPrice":monenybuy,
                "time":time,
                "nowTime":finalltime,
            }
            result.append(datas)
            #print(name,danwei,jibenbi,xianhuisell,monenysell,xianhubuy,monenybuy,time,finalltime)


        # for m in tr.find_all('td'):
        #
        #     if m.get_text()!="交易币":
        #         print(m.get_text())
emp.insert_many(result)