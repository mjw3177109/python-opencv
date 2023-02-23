# list1=[1,5,3,4,2]

list1=[2,4,6,8,10,12]
dict={}
sets=set()
list2=sorted(list1)
print(list2)
target=2
for m in list2:
    for j in list2:
        if abs(j-m)==target:
            newdata=str(m)+"-"+str(j)
            newdata1=str(j)+"-"+str(m)
            if newdata not in dict and newdata1 not in dict:
                sets.add((m,j))
                dict[newdata] = 1

print(sets)
print(dict)
print(len(sets))
# print(int(len(sets)/2))
