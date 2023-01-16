##首先我们知道 栈:是先入后出 后入先出  队列是先入先出
##已经条件 两个栈A,B 结果一个先入先出的队列
##所以实现思路:
##1.先写一个栈
##2.把数据先入到A栈
##3.把A栈的数据出栈后到B栈,此时B栈进行出栈完成了对a栈底元素的删除
##4.这个还需要一些限制 比如先运行了一次b栈里面已经有了数据,这时候就要先把之前的数据出完 然后再把a的数据导入B
##5. 如果b栈出完了数据,A栈没有数据,那这个运行不了返回-1




class Stack:
    def __init__(self):
        self.stack=[]

    def append_in(self,data):
        self.stack.append(data)

    def append_out(self):
        if len(self.stack)>=1:
            return self.stack.pop()
        else:
            return  -1

    def print_stack(self):
        return self.stack

    def get_length(self):
        return len(self.stack)

# stackA=Stack()
# stackB=Stack()
#
# stackA.append_in(2)
# stackA.append_in(3)
# stackA.append_in(4)
# print(stackA.print_stack())
# data =stackA.append_out()
# print(data)

class Squeue(object):
    def __init__(self):
        self.stackA=Stack()
        self.stackB=Stack()

    def append_data(self,data):
        self.stackA.append_in(data)
        # return self.stackA.get_length()

    def get_data(self):
        if self.stackB.get_length()>=1:
            return self.stackB.append_out()
        if self.stackA.get_length() ==0:
            return -1
        for i in range(self.stackA.get_length()):
            data=self.stackA.append_out()
            self.stackB.append_in(data)
        return self.stackB.append_out()


new_data=Squeue()
new_data.append_data(8)
new_data.append_data(822)
new_data.append_data(232)
new_data.append_data(892)
datas =new_data.get_data()
print(datas)
datas =new_data.get_data()
print(datas)

