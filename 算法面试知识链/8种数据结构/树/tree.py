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
    def __iter__(self):
        self.root=None
        self.size=0



