from typing import List
from bintree_helper import *

class Solution:
    # def levelOrderBottom(self, root) -> List[List[int]]:
    #     "DFS, Time: O(n), Space: O(n)"
    #     if root is None: return []
    #     result = []
    #     def dfs(node, level):
    #         if level == len(result):
    #             result.append([])
    #         result[level].append(node.val)
    #         if node.left: dfs(node.left, level+1)
    #         if node.right: dfs(node.right, level+1)
    #     dfs(root, 0)
    #     return result[::-1]
    def levelOrderBottom(self, root) -> List[List[int]]:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return []

        q = deque([root])
        result = []
        while q:
            n = len(q)
            result.append([])
            for _ in range(n):
                node = q.popleft()
                result[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return result[::-1]


root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().levelOrderBottom(root)
assert result == [
  [15,7],
  [9,20],
  [3]
]