"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为0,1或2




"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_o = set()
        rotton_o = set()
        rotton_q = collections.deque()
        # record the fresh and rotton
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = grid[i][j]
                if temp == 1:
                    fresh_o.add((i, j))
                if temp == 2:
                    rotton_o.add((i, j))
                    rotton_q.append((i, j, time))

        while rotton_q:

            i, j, t = rotton_q.popleft()
            time = t
            # up
            if i - 1 >= 0 and (i - 1, j) in fresh_o:
                # become rotton
                fresh_o.remove((i - 1, j))
                rotton_q.append((i - 1, j, t + 1))
            # down
            if i + 1 < len(grid) and (i + 1, j) in fresh_o:
                # become rotton
                fresh_o.remove((i + 1, j))
                rotton_q.append((i + 1, j, t + 1))
            # left
            if j - 1 >= 0 and (i, j - 1) in fresh_o:
                # become rotton
                fresh_o.remove((i, j - 1))
                rotton_q.append((i, j - 1, t + 1))
            # right
            if j + 1 < len(grid[0]) and (i, j + 1) in fresh_o:
                # become rotton
                fresh_o.remove((i, j + 1))
                rotton_q.append((i, j + 1, t + 1))

        if not fresh_o:
            return time
        return -1
