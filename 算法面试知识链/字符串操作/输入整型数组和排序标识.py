"""

描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序

数据范围：


1≤n≤1000  ，元素大小满足


0≤val≤100000
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述：
输出排好序的数字

示例1
输入：
8
1 2 4 9 3 55 64 25
0
复制
输出：
1 2 3 4 9 25 55 64
复制
示例2
输入：
5
1 2 3 4 5
1
复制
输出：
5 4 3 2 1
"""

import sys

newlist = []
for line in sys.stdin:
    a = line.split()
    NumberAll = 0
    order = 0

    if a == []:
        break
    if len(a) > 1:
        newlist = [int(m) for m in a]

    if len(a) == 1:
        if int(a[0]) == 1:
            newlist.sort(reverse=True)
            newstring = ""
            for m in newlist:
                newstring = newstring + str(m) + " "
            print(newstring[:-1])
        elif int(a[0]) == 0:

            newlist.sort()
            newstring = ""
            for m in newlist:
                newstring = newstring + str(m) + " "
            print(newstring[:-1])














