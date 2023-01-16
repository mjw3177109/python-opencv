
host = '182.61.46.244'

import pymongo

client = pymongo.MongoClient(host=host, port=27017, username='admin', password='343340864a')
# 连接数据库
db = client.admin
users = db["questionStore"]

print(db.list_collection_names())  # 获取数据库中所有集合名称

#data = users.find_one()  # 查询单条数据

admins =db["question_store"]
datas = users.find()  # 查询全部数据
for data in datas:
    admins.insert_one(data)

