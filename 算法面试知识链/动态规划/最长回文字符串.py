"""
描述
对于长度为n的一个字符串A（仅包含数字，大小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。


数据范围：

1000
1≤n≤1000
要求：空间复杂度

O(1)，时间复杂度

O(n
2
 )
进阶:  空间复杂度

O(n)，时间复杂度

O(n)
示例1
输入：
"ababc"
复制
返回值：
3
复制
说明：
最长的回文子串为"aba"与"bab"，长度都为3
示例2
输入：
"abbba"
复制
返回值：
5
复制
示例3
输入：
"b"
复制
返回值：
1


"""


"""
题目主要信息：
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度
回文串，指左右对称的字符串
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    def fun(self, s: str, begin: int, end: int) -> int:
        #每个中心点开始扩展
        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            begin -= 1
            end += 1
        #返回长度
        return end - begin - 1
    def getLongestPalindrome(self , A: str) -> int:
        maxlen = 1
        #以每个点为中心
        for i in range(len(A) - 1):
            #分奇数长度和偶数长度向两边扩展
            maxlen = max(maxlen, max(self.fun(A, i, i), self.fun(A, i, i + 1)))
        return maxlen