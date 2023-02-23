"""
描述
明明生成了
N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围：
1≤x≤1000
1≤n≤1000  ，输入的数字大小满足
1≤x≤500
1≤val≤500

"""
import sys


newset=set()
i=0
for line in sys.stdin:
    a = line.split()
    i+=1
    if i==1:
        i+=1
        continue
    newset.add(int(a[0]))

newlist =list(newset)
newlist.sort()
for m in newlist:
    print(m)

