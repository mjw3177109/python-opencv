import requests


def getListdata(CateName):
    datas = requests.get("http://182.61.46.244:8880/category/list")
    datas_json=datas.json()
    finall_datas=[]
    for data_obejct in datas_json["data"]["list"]:
        #print(data_obejct)
        if data_obejct["cateName"] ==CateName:
            finall_datas=data_obejct["secodeCateList"]

    return finall_datas
