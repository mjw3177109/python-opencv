from typing import  List
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        res = []
        self.preOrder(root, res)
        return res

    def preOrder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
