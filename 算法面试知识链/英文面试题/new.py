import requests


def getUsernames(threshold):
    datas = []
    for i in range(2):
        i=i+1
        res = requests.get(url="https://jsonmock.hackerrank.com/api/article_users?page={}".format(i))
        # print(res.json())

        data_list = res.json()["data"]

        for k in data_list:
            # print(k["username"])
            if k["submitted"]>threshold:
                datas.append(k["username"])

    return datas

    # Write your code here

import os
if __name__ == '__main__':
    fptr = open("222.txt", 'w')

    threshold = int(input().strip())

    result = getUsernames(threshold)
    print(result)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()