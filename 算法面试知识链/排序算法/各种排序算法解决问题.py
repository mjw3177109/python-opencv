#算法:输入整型数组,输出从小到大排序的数组


#第一种冒泡排序
def BubbleSort(datalist):
    if len(datalist)>1:
        for i in range(len(datalist)):
            for j in range(i-1):
                if datalist[i] >datalist[j]:
                    datalist[i],datalist[j] =datalist[j],datalist[i]

