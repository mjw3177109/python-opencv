#众所周知双链表就是有两个指针的特殊链表

#不同于单链表 增加了一个向一个节点的指针,在查找方面更好,但是内存增加,而且删除方面变得更加复杂

#老规矩
class Node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None


class DobuleLinkedList:
    def __init__(self):
        self._head=None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False


    def get_length(self):
        number=0
        cur =self._head
        while cur :
            number+=1
            cur =cur.next
        return number

    def get_items(self):
        """遍历链表"""
        cur =self._head
        while cur is not None:
            yield cur
            #指针下移
            cur =cur.next

    #头插法
    def add_item(self,item):
        node =Node(item)
        if self.is_empty():
            self._head =node
        else:
            node.next =self._head
            self._head.prev =node
            self._head =node

    #尾插法
    def append_item(self,item):
        node =Node(item)
        cur =self._head
        if self.is_empty():
            self._head=node
            return
        #找到最后一个节点
        while cur.next:
            cur =cur.next
        cur.next = node
        node.prev=cur

    def insert(self,pos,item):
        if pos<=0:
            self.add_item(item)
        elif pos >len(self)-1:
            self.append_item(item)

        else:
            node =Node(item)
            number =0
            cur =self._head
            while number <pos -1:
                number+=1
                cur=cur.next
            node.next=cur.next
            cur.next.prev =node
            node.prev =cur
            cur.next =node


    def find(self,item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next

        return False

    def remove(self, item):
        if self.is_empty():
            return
        cur =self._head
        while cur:
            if cur.item == item:
                if cur ==self._head:
                    self._head = cur.next
                    if cur.next:
                        cur.next.prev=None
                else:
                    cur.prev.next = cur.next
                    #如果是最后一个节点
                    if cur.next:
                        cur.next.prev = cur.prev
                return
            else:
                cur=cur.next






##测试
newlist =DobuleLinkedList()
newlist.append_item(1)
newlist.append_item(2)
newlist.append_item(3)
# for i in newlist.get_items():
#     print(i.item)

newlist.add_item(7)
# for i in newlist.get_items():
#     print(i.item)
newlist.remove(2)
for i in newlist.get_items():
    print(i.item)