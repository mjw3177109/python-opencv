"""

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。


例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

提示：

节点总数 <= 1000


"""


"""
时间复杂度 

O(N) ： 

N 为二叉树的节点数量，即 BFS 需循环 

N 次。
空间复杂度 

O(N) ： 最差情况下，即当树为平衡二叉树时，最多有 

N/2 个树节点同时在 queue 中，使用 

O(N) 大小的额外空间。


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res

