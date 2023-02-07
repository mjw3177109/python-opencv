#在单链表中 查找是最费劲的，如果我们要找到最后一个元素就得从头到尾一个一个得找,
# 当我们找到最后一个元素,这时候我们还想找前面得节点,又得重新开始
#所以我们希望单链表遍历到最后一个节点后下一个节点就是头节点 这样就可以不间断得遍历下去,
#于是就有了循环链表

#还是老规矩创建节点
class Node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None

#这时候开始创建循环链表即最后一个节点链接到头节点
class CircleList:
    def __init__(self):
        self.head=None
    #尾部插入
    def append_ele(self,ele):
        node =Node(ele)
        #如果头节点是空自己指向自己
        if self.head is None:
            self.head=node
            node.next =self.head
        else:
            cur =self.head
            #找到最后一个节点
            while cur.next !=self.head:
                cur =cur.next
            #新节点指向头节点
            node.next=cur.next
            cur.next =node

    def get_NodeLength(self):
        number = 0
        if self.head is None:
            return number
        cur =self.head
        if cur.next ==self.head:
            return 1

        while cur.next !=self.head:
            number +=1
            cur =cur.next

            #还要加上最后一个元素
        number+=1
        return number

    def delete_ele(self,ele):
        if self.head is None:
            return "没有元素可以删除"
        if self.head.next == self.head:
            self.head=None

        cur =self.head

        ##如果删除的是头节点
        if cur.ele==ele:
            # 找到最后一个节点
            while cur.next != self.head:
                cur = cur.next

            self.head=self.head.next
            cur.next =self.head
            return True
        else:
            pre_node = None
            #找出该节点
            while cur.next != self.head:
                if cur.ele == ele:
                    pre_node.next = cur.next
                    return True
                else:
                    pre_node = cur
                    cur = cur.next
            if cur.ele == ele:
                pre_node.next = cur.next
                return True
            else:
                return False

    #前插入
    def insert_ele(self,pos,ele):
        node=Node(ele)
        if pos ==0:
            return "没有第0个,请输入1"
        pos =pos-1
        #如果是头节点
        if pos ==0:
            cur =self.head
            #找到最后一个节点
            while cur.next != self.head:
                cur=cur.next
            node.next = self.head
            self.head=node
            cur.next=node

        else:
            if 0<pos <= self.get_NodeLength():
                #找到该位置节点
                cur =self.head
                pre_node =None
                for i in range(pos):
                    pre_node = cur
                    cur =cur.next
                print(pre_node)
                print(cur)
                pre_node.next=cur.next
            else:
                return "插入超出范围"



    #按位置删除
    def delete_posele(self,pos):
        #如果是头节点
        pos=pos-1
        if pos==0:
            cur= self.head
            # 找到最后一个节点
            while cur.next != self.head:
                cur=cur.next
            self.head =self.head.next
            cur.next=self.head
            return True
        else:
            if 0<pos <= self.get_NodeLength():
                # 找到该位置节点
                cur = self.head
                pre_node = None
                for i in range(pos):
                    pre_node = cur
                    cur = cur.next
                pre_node.next = cur.next
            else:
                return "删除超出范围"



    def find_ele(self, ele):
        """查找元素是否存在"""
        cur =self.head
        if cur.ele==ele:
            return True
        else:
            while cur.next != self.head:
                if cur.ele == ele:
                    return True
                else:
                    cur =cur.next
            if cur.ele == ele:
                return True
            else:
                return "数据不存在"

    def get_items(self):
        """遍历链表"""
        cur =self.head

        if self.get_NodeLength()==0:
            return
        if self.get_NodeLength()==1:
            yield cur
            return
        while  cur.next !=self.head:
            yield cur
            #指针下移
            cur =cur.next
        else:
            yield cur
            return







#测试
newlist =CircleList()
newlist.append_ele(1)
# print(newlist.get_NodeLength())
# for i in newlist.get_items():
#     print(i.ele)
newlist.append_ele(2)
newlist.append_ele(3)

# print(newlist.find_ele(3))

# print(newlist.delete_ele(2))

print(newlist.delete_posele(2))

for i in newlist.get_items():
    print(i.ele)

# print(newlist.get_NodeLength())

# newlist.delete_posele(1)
# for i in newlist.get_items():
#     print(i.ele)

# newlist.insert_ele(2,5)
# for i in newlist.get_items():
#     print(i.ele)
# newlist.insert_ele(0,5)
# for i in newlist.get_items():
#     print(i.ele)

