"""
描述
数据表记录包含表索引index和数值value（int范围的正整数），
请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，
输出按照index值升序进行输出。
提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4
复制
输出：
0 3
1 2
3 4
复制
示例2
输入：
3
0 1
0 2
8 9
复制
输出：
0 3
8 9



"""

import sys



# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]))

# newdict={}
#
#
# a=int(input())
#
# if len(newdict)>=1:
#     if 1 in newdict:
#         newdict[1].append(2)
#     else:
#         newdict[1]=[]


import sys

flag = True

newdict = {}
newdict2={}
for line in sys.stdin:
    a = line.split()
    if flag:
        data = int(a[0])
        flag = False
        continue
    if a==[]:
        break
    data = int(a[0])
    data2=int(a[1])

    if len(newdict) > 1:
        if data in newdict:
            newdict[data].append(data2)
        else:
            newdict[data] = []
            newdict[data].append(data2)
    else:
        newdict[data] = []
        newdict[data].append(data2)

# print(newdict,"224")
for key,value in newdict.items():
    res =0
    for v in value:
        res= res +int(v)
    newdict2[key]=res

newdict3=sorted(newdict2.items(),key=lambda x:x[1])
for k,v in newdict3:
    print(k,v)




