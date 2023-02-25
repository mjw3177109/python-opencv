"""

有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。



"""
import itertools
from typing import List


# class Solution:
#     def permutation(self, S: str) -> List[str]:
#         return ["".join(e) for e in set(itertools.permutations(S))]


class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 1:
            return [S]
        elif len(S) == 2:
            if S[0] == S[1]:
                return [S]
            else:
                return [S, S[::-1]]
        else:
            ans = set()
            visited = set()
            for i in range(len(S)):
                ch = S[i]
                if ch not in visited:
                    visited.add(ch)
                    for other in self.permutation(S[:i] + S[i + 1:]):
                        ans.add(ch + other)
            return list(ans)
