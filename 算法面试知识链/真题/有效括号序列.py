"""
描述
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

数据范围：字符串长度
10000
0≤n≤10000
要求：空间复杂度
O(n)，时间复杂度

O(n)
示例1
输入：
"["
复制
返回值：
false
复制
示例2
输入：
"[]"
复制
返回值：
true

"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#

# write code here
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        strs=[]
        for m in s:
            if m =="(":
                strs.append(")")
            elif m =="[":
                strs.append("]")
            elif m =="{":
                strs.append("}")
            elif len(strs)==0:
                return False
            elif(strs[-1] ==m):
                strs.pop()


        return len(strs)==0

