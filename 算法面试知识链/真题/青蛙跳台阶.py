"""

描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

数据范围：

1≤n≤40
要求：时间复杂度：

O(n) ，空间复杂度：

O(1)

"""
# def jumpFloor(number):
#     if 1<=number<=40:
#         if number == 1:
#             return 1
#         elif number == 2:
#             return 2
#         else:
#             return jumpFloor(number - 1) + jumpFloor(number - 2)
#
number=4
# data =jumpFloor(number)
# print(data)

def jumpFloor(number: int) ->int:
    # write code here
    if 1 <= number <= 40:
        if number <= 2:
            return number
        else:
            res = 0
            a = 1
            b = 2
            for i in range(2, number):
                res = a + b
                a = b
                b = res
            return res

data=jumpFloor(number)
print(data)