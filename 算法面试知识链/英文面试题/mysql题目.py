
import requests

threshold=2



import os
if __name__ == '__main__':
    fptr = open("123.txt", 'w')

    threshold = int(input().strip())

    res = requests.get(url="https://jsonmock.hackerrank.com/api/article_users?page={}".format(threshold))

    data_list = res.json()["data"]
    datas=[]

    for k in data_list:
        print(k["username"])
        datas.append(k["username"])

    print(datas)

    result = datas

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

#
# projectCosts=[2,4,6,8,10,12]
# countNumber =0
# set1=set()
# set2={}
# set3=[]
# target=2
#
# countNewNumber=0
#
#
# for m in projectCosts:
#     for j in projectCosts:
#         if m==j:
#             continue
#         if j==target:
#             continue
#
#         if len(set1)>1:
#             if (m not in set2) and (j not in set2):
#                 set1.add((m, j))
#
#         else:
#             set2[m]=1
#             set2[j]=1
#             set1.add((m,j))
#
#
#
# for h in set1:
#     for t in set1:
#         if h[0]==t[1] and h[1]==t[0]:
#             countNewNumber +=1














# print(set1)
# countNumber=len(set1)
# print(countNewNumber)
# print(countNumber)
