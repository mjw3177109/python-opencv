#树是一种数据结构
#比如目录结构
#类似这种--11
#        --222
#           --444
#         --333
#它由n个节点组成,可以递归的集合
##如果n=0,它就是一个空树
#如果n>0那么它就是存在1个节点为跟节点 其他节点可以分为m个集合的树,当然每个集合本身也是一棵树
#可以把它理解为现实中树的根 从一个从出发往四面八方扩展
#根节点、叶子节点
#树的深度
#树的度
#孩子节点/父子节点
# 子树

######
#首先创建树的节点

#####

class Node:
    def __init__(self,value):
        self.value =value
        self.children=[]
        self.parent =None

####
#然后写一个树
####

class Tree:
    def __init__(self):
        self.root=None
        self.size=0

    def append_data(self,value,parent=None):
        if parent ==None:
           self.root =Node(value)
           return
        else:

            data =Node(value)
            cur =self.root
            if self.root.value ==parent:
                cur.children.append(data)
                data.parent=cur
            else:
                if cur.children!=[]:
                    self.find_data(cur.children,data,parent)

    def find_data(self,nodes,item,parent):
        if nodes!=[]:
            for data in nodes:
                if data.value == parent:
                    item.parent = data
                    data.children.append(item)

                    return
                if data.children!=[]:
                    self.find_data(data)

    def prints(self):
        cur =self.root
        if cur.children==[]:
            print(cur.value)
            return
        else:
            tips ="-"
            print(cur.value,tips)
            self.print_data(cur.children,tips)

    def print_data(self,nodes,tips):
        if nodes!=[]:
            tips = tips + "-"
            for data in nodes:

                print(data.value,tips)
                if data.children!=[]:
                    self.print_data(data.children,tips)






##测试

tree =Tree()

tree.append_data("1")
# tree.prints()
tree.append_data("2","1")
tree.append_data("3","1")
tree.prints()
tree.append_data("4","3")
tree.prints()

"""

1 -
2 --
3 --
4 ---

"""


