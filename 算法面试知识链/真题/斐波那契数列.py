"""
描述
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
斐波那契数列是一个满足

fib(x)={
1
fib(x−1)+fib(x−2)

x=1,2
x>2
  的数列
数据范围：

1≤n≤40
要求：空间复杂度

O(1)，时间复杂度

O(n) ，本题也有时间复杂度

)
O(logn) 的解法

"""
def getFib(number):
    if number ==1:
        return 1
    elif number ==2:
        return 2
    else:
        return getFib(number-1)+getFib(number-2)