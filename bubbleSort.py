from decoractor import timing


class BubbleSort(object):
    def __init__(self, unsortlist):
        self.unsortlist = unsortlist

    @timing
    def deSort(self):
        if len(self.unsortlist) <= 1:
            return "not valid unsortlist,length is not enough"
        for i in range(len(self.unsortlist)):
            for j in range(len(self.unsortlist) - i - 1):
                if self.unsortlist[j] <= self.unsortlist[j + 1]:
                    self.unsortlist[j], self.unsortlist[j + 1] = self.unsortlist[j + 1], self.unsortlist[j]


if __name__ == '__main__':
    # 输入要排序的列表,
    # 返回降序排序后的列表
    test_list = [12, 34, 1, 45, 67, 23, 52]
    bubble = BubbleSort(test_list)
    bubble.deSort()
    print(test_list)
