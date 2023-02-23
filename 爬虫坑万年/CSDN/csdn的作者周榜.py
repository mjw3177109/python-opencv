host = '110.41.18.114'
import pymongo

client = pymongo.MongoClient(host=host, port=27017, username='admin', password='343340864aA')
# 连接数据库
db = client.admin
emp =db.csdn_data
# print(db.list_collection_names())  # 获取数据库中所有集合名称
import requests
import datetime


def get_info(page):
    result =[]
    try:
        url ="https://blog.csdn.net/phoenix/web/v2/rank?rankType=weekly_author&page={}&pageSize=25".format(page)
        headers ={
            "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        }
        r =requests.get(url,headers=headers)
        if r.status_code ==200:
            weeklyRankListTeam =r.json()["data"]["list"]
            for m in weeklyRankListTeam:
                result.append({
                    "currentRank": m["currentRank"],
                    "hotRankScore": m["hotRankScore"],
                    "userName": m["userName"],
                    "nickName": m["nickName"],
                    "avatarUrl": m["avatarUrl"],
                    "loginUserIsFollow": m["loginUserIsFollow"],
                    "lastRank": m["lastRank"],
                    "vipIcon": m["vipIcon"],
                    "companyBlog": m["companyBlog"],
                    "companyBlogIcon": m["companyBlogIcon"],
                    "flag": m["flag"],
                    "flagIcon": m["flagIcon"],
                    "level": m["level"],
                    "levelIcon": m["levelIcon"],
                    "fansCount": m["fansCount"],
                    "diggCount": m["diggCount"],
                    "vip": m["vip"],
                    "time":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),


                })
            # print(weeklyRankListTeam)
            return result
        else:
            return []
    except Exception as e:
        print(e)
        return []

# datas=get_info(1)
# print(datas)
#获取当前时间
# now =datetime.datetime.now()
# print(now)

#插入
#emp.insert_many()
for i in range(4):
    i=i+1
    datas_list = get_info(i)
    emp.insert_many(datas_list)

