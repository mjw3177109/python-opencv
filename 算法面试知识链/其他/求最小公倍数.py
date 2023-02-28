"""
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围：

100000

1≤a,b≤100000
输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。

示例1
输入：
5 7
复制
输出：
35
复制
示例2
输入：
2 4
复制
输出：
4


"""
import sys

def check(a,b):
    number =max(a,b)
    addnumber =max(a,b)
    while True:
        if number %a ==0 and number %b ==0:
            break
        else:
            number =number+addnumber
    print(number)

for line in sys.stdin:
    a = line.split()
    if a ==[]:
        break
    x,y=int(a[0]),int(a[1])
    check(x,y)
