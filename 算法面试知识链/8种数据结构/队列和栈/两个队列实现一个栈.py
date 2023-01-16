

class NewQueue(object):

    def __init__(self):
        self.queue =[]


    def add_data(self,data):
        self.queue.append(data)

    def delete_data(self):
        if len(self.queue)==0:
            return -1
        return self.queue.pop(0)

    def print_data(self):
        return self.queue

    def get_length(self):
        return len(self.queue)


###test
newqueue =NewQueue()
newqueue.add_data(1)
newqueue.add_data(10)
newqueue.add_data(11)
# print(newqueue.print_data())
# data=newqueue.delete_data()
# print(data)
# print(newqueue.print_data())

class newStack(object):
    def __init__(self):
        self.queueA = NewQueue()
        self.queueB = NewQueue()


    def add_data(self,data):
        self.queueA.add_data(data)

    def del_data(self):
        if self.queueA.get_length()==0:
            return -1
        if self.queueA.get_length()==1:
            return self.queueA.delete_data()
        for i in range(self.queueA.get_length()-1):
            self.queueB.add_data(self.queueA.delete_data())

        return_data=self.queueA.delete_data()
        self.queueA,self.queueB =self.queueB,self.queueA
        return return_data


    def print_data(self):
        return self.queueA.print_data()

##test测试

newstack=newStack()

newstack.add_data(2)
newstack.add_data(5)
newstack.add_data(7)
print(newstack.print_data())
datas=newstack.del_data()
print(datas)
print(newstack.print_data())

