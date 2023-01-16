"""

链表是一种在存储单元上非连续、非顺序的存储结构。
数据元素的逻辑顺序是通过链表中的指针链接次序实现。
链表是由一系列的结点组成，结点可以在运行时动态生成。
每个结点包含两部分：数据域与指针域。
数据域存储数据元素，指针域存储下一结点的指针
"""

"""
单向链表也叫单链表，是链表中最简单的形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。
这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值
"""
"""
定义结点

结点的数据结构为数据元素(item)与 指针(next)

2、定义链表

链表需要具有首地址指针head。
"""

class Node(object):
    def __init__(self,item):
        self.item=item
        self.nextNode=None


class SingleLinkList(object):
    def __init__(self):
        self._head=None

    def is_empty(self):
        return self._head is None

    def get_length(self):
        node =self._head
        count =0
        while node is not None:
            count+=1
            #指针下移动
            node= node.nextNode
        return count

    def get_items(self):
        """遍历链表"""
        node =self._head
        while node is not None:
            yield node
            #指针下移
            node =node.nextNode

    def add_item(self,item):
        """头部添加元素"""
        node =Node(item)
        node.nextNode =self._head
        self._head=node

    def append_item(self,item):
        """尾部添加"""
        node =Node(item)
        #有个判断是否是一个空链表
        if self.is_empty():
            self._head =node
        else:
            #不是空要找到最尾部的那个节点 要从头找起
            cur_node =self._head
            while cur_node.nextNode is not None:
                cur_node=cur_node.nextNode
            cur_node.nextNode=node

    def insert(self,pos,item):
        """指定位置插入元素"""
        if pos <=0:
            self.add_item(item)
        elif pos >(self.get_length()-1):
            self.append_item(item)
        else:
            node =Node(item)
            cur_node =self._head
            #找到指定位置前后的节点 断开然后连上自己
            for i in range(pos -1):
                cur_node=cur_node.nextNode
            node.next =cur_node.nextNode
            cur_node.next=node
    def remove_item(self,item):
        if not item in self.get_items():
            return "没有找到该节点"

        #也是从头开始找起,这时候你就发现优缺点了把 虽然插入删除数据自由灵活多变  但是查找数据相当麻烦
        cur_node =self._head
        pre_node =None
        while cur_node is not None:
            if cur_node.item ==item:
                #如果没有前节点那么就是头节点,删除头节点就是把头节点指向下一个节点
                if not pre_node:
                    self._head=cur_node.nextNode
                else:
                    #如果有前节点 就是把前节点的下一个节点指向当前节点的下一个节点
                    pre_node.nextNode=cur_node.nextNode
                return  True


            else:
                #下移动
                pre_node =cur_node
                cur_node=cur_node.nextNode



    def find_item(self,item):
        """查找元素是否存在"""
        return item in self.get_items()





##测试
newlist =SingleLinkList()
newlist.append_item(1)
newlist.append_item(2)
newlist.append_item(3)
# for i in newlist.get_items():
#     print(i.item)

print("#####")
# newlist.remove_item(1)
# for i in newlist.get_items():
#     print(i)

class Solution:
    ###1-2-3-none是正常顺序
    ###反顺序3->2->1->none

    def ReverseList(self , head: Node) -> Node:
        # write code here
        if head == None:
            return head

        cur =head
        #要反转的尾节点
        pre =None

        while cur:
            #在这里就是pre=none cur=1
            tmp =cur.nextNode
            #保存2-3位置
            ##把当前的节点的下一个节点设置为none
            cur.nextNode=pre
            ###pre节点为当前节点
            pre =cur
            ##现在就是 1>none  tmp 2->3
            ##现在开始接上2-3
            cur =tmp
            ##这样就是 1>none>2->3
            ##然后cur=2 pre=1

            ##然后迭代一次就变成 2->1->none->3

        return pre

solution=Solution()
data=solution.ReverseList(newlist._head)
##打印出所有逆反的数据
cur =data
while cur is not None:
    print(cur.item)
    cur =cur.nextNode














