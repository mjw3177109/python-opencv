#散列表 英文名hash table,也叫哈希表
#它也是一种线性表的存储结构,它是由一个寻址表和一个哈希函数组成
#主要的方法是通过哈希函数来计算数据存储位置,通常是将关键字k作为自变量
#一般都支持insert(key,value)
#get(key),delet(key) 增查删动作

#既然是线性结构的表那么查找方式是不是和链表一样呢？
#
#第一:直接寻址表
#当我们的key的数量很小的时候,直接寻址是最快的方法-一个一个的算
#比如我们用key 0-10 建立来一个列表[0,1,2,3,4,5,6,7,8,9,10]🇺每个位置都是空的
#那么整块是比较小的直接通过哈希函数计算即可
#缺点也很明显:
#当key的值很大的时候 需要耗费大量的内存来生成对应的空间
#无法处理关键字不是数字的情况

#第二哈希查询法(key为k的元素放到k位置上)
#做法构建大小为m的寻址表T
#key作为k的元素放到哈希函数h(k)位置上-即[0,m-1]
#比如我们现在有这个一个长度为10的哈希表,哈希的函数为h(k)=k%10
#要存储的元素为5,20,11,7
#那么整块的结构为
# [(20),(11),(),(),(),(5),(),(7),(),()]
# [0,1,2,3,4,5,6,7,8,9]
#
#但是由于哈希表的大小是有限的 而存储的值是无法预计的
#所以对于哈希函数都会出现两个不同元素映射到同一位置
#这种情况叫哈希冲突 比如h(10)=h(20)=h(30)
#解决方法有开放寻址法：如果哈希函数返回的位置已经有值,则可以向后探查新的位置来存储这个值
#线性探查：如果位置x被占用 则探查x+1,x+2
#二次探查：如果位置x被占用,则探查x+（1的平方）或x-（1的平方）
#二度哈希:假如有n个哈希函数,当使用第一个哈希函数发生冲突,则使用第二个哈希函数
#拉链表
#哈希位置存的不是一个元素而是一个链表,这样每次冲突发生的时候,冲突的元素将会被加到该位置链表的最后
#哈希函数一般有h(k)=k%m
#乘法哈希函数
#h(k)=floor(m*(A*key%1))
#全域哈希函数
#ha,b(k)=((a*key+b)mod p)mode m a,b=1,2..,p-1

#python中的主要代表就是字典与集合,通过key,value来存储数据，通过key找到对应数据而不是直接通过下标
#里面能存储的类型是多样而不是单一类型
#其中的应用最熟悉的应该是md5算法(把任意长度的数据映射为128位哈希值)用在cookie中加密用户信息
###论如何实现一个拉链法哈希表
#它也是线性的表,
#所以先创建一个哈希表节点先-先从节点开始然后再hash节点
class Node:
    def __init__(self,item=None):
        self.item=item
        self.next =None



class LinkListNode:
    # 一个节点就是一个链表
    def __init__(self):
        #链表头和尾
        self.head=None
        self.tail=None


    def find(self,data):
        """遍历链表"""
        cur =self.head
        while cur is not None:
            if cur.item == data:
                return True
            else:
                cur=cur.next
        else:
            return False

    def find_items(self):
        """遍历链表"""
        node =self.head
        while node is not None:
            yield node

            #指针下移
            node =node.next

    def append(self,data):
        newNode= Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def printData(self):
        list1=[]
        for i in self.find_items():
            list1.append(i.item)
        print( "(("+",".join(map(str,list1))+"))")


#创建哈希表
class HashTable:
    def __init__(self,size=10):
        self.size =size
        self.T =[LinkListNode() for h in range(self.size)]
    def h(self,k):
        return k%self.size
    def find(self,k):
        i=self.h(k)
        return self.T[i].find(k)
    def insert(self,k):
        index =self.h(k)
        if not self.find(index):
            self.T[index].append(k)
        else:
            print("不能重复插入相同的元素")
    def getLength(self):
        return self.size








hash_table =HashTable(30)
for i in range(12):
    hash_table.insert(i)



print(hash_table.find(1))
for h in range(hash_table.getLength()):

    for k in hash_table.T[h].find_items():
        print(h,k.item)
    # hash_table.T[h].printData()














