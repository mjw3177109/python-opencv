# coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     if a==[]:
#         break
#     print(int(a[0]) + int(a[1]))


# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

# import sys
#
#
# def find_twoNumber(values, p_max):
#     newlist = set()
#     for i in range(len(values)):
#         for j in range(len(values)):
#             if values[i] + values[j] < p_max:
#                 newlist.add((values[i], values[j]))
#     return newlist
#
#
# def check_max(newlist, values, p_max):
#     for m in newlist:
#         cur = p_max - (int(m[0]) + int(m[1]))
#         for j in values:
#             if j == cur:
#                 return True
#
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     # 读取每一行
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#
#     p_max = int(sys.stdin.readline().strip())
#     nums = p_max
#     newlist = []
#     for v in values:
#         if v > p_max:
#             p_max = v
#     if p_max != nums:
#         print(0)
#     else:
#         print(p_max)
#
#











