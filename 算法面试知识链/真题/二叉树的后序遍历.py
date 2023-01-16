from typing import List
import sys

##### python默认的递归深度是很有限的，大概是900多的样子，当递归深度超过这个值的时候，就会引发这样的一个异常：RuntimeError: maximum recursion depth exceeded。

#解决的方式是手工设置递归调用深度，方式为
sys.setrecursionlimit(100000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def postorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        res =[]
        self.postOrder(root,res)
        return res

    def postOrder(self,root,res):
        if not root:
            return None
        self.postOrder(root.left, res)
        self.postOrder(root.right, res)
        res.append(root.val)