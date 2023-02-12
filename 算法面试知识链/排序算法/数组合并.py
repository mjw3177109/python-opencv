#数组合并:输入2个已经排好序的数组,返回数组排序后合并成1个数组


def merge_sort(a, b):
    ret = []
    i = j = 0
    while len(a) >= i + 1 and len(b) >= j + 1:
        if a[i] <= b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
    if len(a) > i:
        ret += a[i:]
    if len(b) > j:
        ret += b[j:]
    return ret

if __name__ == '__main__':
    a = [1,3,4,6,7,78,97,190]
    b = [2,5,6,8,10,12,14,16,18]
    print(merge_sort(a, b))
