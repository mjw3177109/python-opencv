"""
描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足
1≤n≤20  ，保证输入的字符串中仅出现小写字母
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述：
删除字符串中出现次数最少的字符后的字符串。

示例1
输入：
aabcddd
复制
输出：
aaddd


"""
import sys


newdict={}
for line in sys.stdin:
    a = line.split()
    if a ==[]:
        break
    for m in a[0].strip():
        if len(newdict)>0:
            if m in newdict:
                newdict[m]+=1
            else:
                newdict[m]=1
        else:
            newdict[m]=1

    newvalues=a[0].strip()
    newlist = []
    minvalue=min(newdict.values())
    for k,v in newdict.items():
        if v==minvalue:
            newvalues=newvalues.replace(k,"")
    print(newvalues)




