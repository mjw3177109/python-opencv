
"""

给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）
要求：空间复杂度
O(n)，时间复杂度
O(nlogn)
"""
# numbers=[2,1,9,4,4,56,90,3]
# target=8

numbers=[0,2,3,0]
target=0



def start(numbers,target):
    newlist=[]
    newdict={}
    for index,value in enumerate(numbers):
        data2=target-value
        if data2 in newdict:
            newlist.append(newdict[data2]+1)
            newlist.append(index+1)
            break
        newdict[value] =index
    return sorted(newlist)


#     newlist.append(newdatas2[h][1])

    # print(h[1])



# datas=start(numbers,target)
# print(datas)


def twoSum( numbers , target ):
        # write code here
    ls=[0,0]
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                # ls.append(i+1)
                # ls.append(j+1)
                ls[0]=i+1
                ls[1]=j+1
                return ls

datas=twoSum(numbers,target)

print(datas)