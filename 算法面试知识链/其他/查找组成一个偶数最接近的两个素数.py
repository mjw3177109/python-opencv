"""

描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

数据范围：输入的数据满足


4≤n≤1000
输入描述：
输入一个大于2的偶数

输出描述：
从小到大输出两个素数

示例1
输入：
20
复制
输出：
7
13
复制
示例2
输入：
4
复制
输出：
2
2

"""


def isPrime(num):
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
        else:
            pass
    return True


def solution(left, right):
    while left >= 0 and right <= n - 1:
        if not isPrime(left) or not isPrime(right):
            left -= 1
            right += 1
        else:
            print(left)
            print(right)
            break


while True:
    try:
        n = int(input())
        solution(int(n / 2), int(n / 2))

    except:
        break
