"""
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。

数据范围：区间组数

0≤n≤2×10
5
 ，区间内 的值都满足

0≤val≤2×10
5

要求：空间复杂度

O(n)，时间复杂度

O(nlogn)
进阶：空间复杂度

O(val)，时间复杂度
O(val)
示例1
输入：
[[10,30],[20,60],[80,100],[150,180]]
复制
返回值：
[[10,60],[80,100],[150,180]]
复制
示例2
输入：
[[0,10],[10,20]]
复制
返回值：
[[0,20]]




"""
from typing import List


class Interval:
   def __init__(self, a=0, b=0):
       self.start = a
       self.end = b

newlist=[[10,30],[20,60],[80,100],[150,180]]
datas=[]
datas.append(Interval(10,30))
datas.append(Interval(20,60))
datas.append(Interval(80,100))
datas.append(Interval(150,180))
print(datas[0].start)

class Solution:

    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        intervals = sorted(intervals, key = lambda x: x.start)
        res=[]
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])


            else:

                if res[-1].end >=intervals[i].start:
                    res[-1].end =max(res[-1].end,intervals[i].end)

                else:
                    res.append(intervals[i])
                    print(intervals[i].start, intervals[i].end)

        return res


data =Solution().merge(datas)
# newlist3=[]
# for m in data:
#     newlist3.append([m.start,m.end])
# print(newlist3)



