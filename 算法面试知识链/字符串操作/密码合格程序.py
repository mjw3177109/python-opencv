"""

密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足


1≤n≤100
输入描述：
一组字符串。

输出描述：
如果符合要求输出：OK，否则输出NG

示例1
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
复制
输出：
OK
NG
NG
OK
"""

import sys


def check(s):
    if len(s)<=8:
        print("NG")
        return
    z,x,c,v =0,0,0,0
    for k in s:
        if ord("a")<=ord(k)<=ord('z'):
            z=1
        elif ord("A")<=ord(k)<=ord("Z"):
            x=1
        elif ord("0")<=ord(k)<=ord("9"):
            c=1
        else:
            v=1
    if z+x+c+v <3:
        print("NG")
        return
    for i in range(len(s)-3):
        if len(s.split(s[i:i+3]))>=3:
            print("NG")
            return
    print("OK")


for line in sys.stdin:
    a = line.split()
    if a==[]:
        break
    s= a[0].strip()
    check(s)



