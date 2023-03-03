"""
所谓的二叉树Binary Tree 就是它的子树是有序的并且每个节点至多有两棵子树的树
其中又分为满二叉树,完全二叉树,排序二叉树,平衡二叉树,退化树,斜二叉树,霍夫曼树,B树,堆heap

"""


"""
二叉树的遍历常见的有四种,先序遍历,中序遍历,后序遍历,层序遍历

"""
"""
这一次我们先来实现一个二叉树
"""

class Node(object):
    def __init__(self,item):
        self.item =item
        self.left =None
        self.right=None

class BinaryTree(object):
    def __init__(self):
        self.root=None

    def append(self,item):
        node =Node(item)
        if self.root is None:
            self.root =node
            return
        queue = [self.root]
        while queue:
            cur =queue.pop(0)
            if cur.left ==None:
                cur.left =node
                return
            else:
                queue.append(cur.left)

            if cur.right==None:
                cur.right =node
                return
            else:
                queue.append(cur.right)
    #层序遍历
    def print_Node(self):
        if self.root is None:
            return 0
        queue = [self.root]
        while queue:
            cur =queue.pop(0)
            print(cur.item,end="")
            if cur.left !=None:
                queue.append(cur.left)
            if cur.right !=None:
                queue.append(cur.right)

    #前序遍历
    def print_Front(self,node):
        if node is None:
            return
        print(node.item,end="")
        self.print_Front(node.left)
        self.print_Front(node.right)



    #中序遍历
    def print_Middle(self,node):
        if node ==None:
            return
        self.print_Middle(node.left)
        print(node.item,end=" ")
        self.print_Middle(node.right)

   #后序遍历
    def print_Rgint(self, node):
        if node == None:
            return
        self.print_Rgint(node.left)
        self.print_Rgint(node.right)
        print(node.item, end=" ")



















binary =BinaryTree()
binary.append(1)
binary.append(3)
binary.append(4)
binary.append(5)
binary.append(6)
binary.print_Node()
print("")
binary.print_Front(binary.root)
print("")
binary.print_Middle(binary.root)
print("")
binary.print_Rgint(binary.root)

#练习
"""
剑指offer32题
描述
不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。例如输入{8,6,10,#,#,2,1}，如以下图中的示例二叉树，则依次打印8,6,10,2,1(空节点不打印，跳过)，请你将打印的结果存放到一个数组里面，返回。

数据范围:
0<=节点总数<=1000
-1000<=节点值<=1000
示例1
输入：
{8,6,10,#,#,2,1}
复制
返回值：
[8,6,10,2,1]
复制
示例2
输入：
{5,4,#,3,#,2,#,1}
复制
返回值：
[5,4,3,2,1]

"""

class TreeNode(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

from typing import List

#{8,6,10,#,#,2,1}
class Solution:

    def __init__(self):
        self.root =None

    def addDataToTree(self,item):
        node =TreeNode(item)
        if self.root==None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left ==None:
                cur.left=node
                return
            else:
                queue.append(cur.left)
            if cur.right ==None:
                cur.right=node
                return
            else:
                queue.append(cur.right)




    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        newlist =[]
        queue =[root]
        while queue:
            cur =queue.pop(0)
            if cur.item !="#":
                newlist.append(int(cur.item))
            if cur == None:
                break
            if cur.left!=None:
                queue.append(cur.left)
            if cur.right!=None:
                queue.append(cur.right)
        return newlist


strs="{8,6,10,#,#,2,1}"
newstrs=strs.replace("{","").replace("}","").split(",")
solution=Solution()
for m in newstrs:
    solution.addDataToTree(m)
newlist =solution.PrintFromTopToBottom(solution.root)
print(newlist)

# print(newstrs)