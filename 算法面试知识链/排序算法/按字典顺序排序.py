"""

描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。

数据范围：

1≤n≤1000  ，字符串长度满足


1≤len≤100
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入：
9
cap
to
cat
card
two
too
up
boat
boot
复制
输出：
boat
boot
cap
card
cat
to
too
two
up


"""

# list1=["cap",
# "to",
# "cat",
# "card",
# "two",
# "too",
# "up",
# "boat",
# "boot"]
#
# newdict={}
# for m in list1:
#     newdict[m]=1
#
# newdict2 =sorted(newdict.items(),key=lambda x:x[0] )
# print(newdict2)
import sys

newdict = []
flag = True
for line in sys.stdin:
    a = line.split()
    if flag:
        data = int(a[0])
        flag = False
        continue
    if a == []:
        break
    data = a[0]
    newdict.append(data)

newdict2 = sorted(enumerate(newdict), key=lambda x: x[1])
for k in newdict2:
    print(k[1])
