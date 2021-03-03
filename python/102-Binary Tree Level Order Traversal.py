from typing import List
from bintree_helper import *
from collections import deque

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        "Level by Level Traversal using BFS, Time: O(n), Space: O(n)"
        if root is None: return []
        q = deque([root])
        result = []
        while q:
            sz = len(q)
            result.append([0]*sz)
            for i in range(sz):
                node = q.popleft()
                result[-1][i] = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return result
    # def levelOrder(self, root) -> List[List[int]]:
    #     "Level by Level Traversal using DFS, Time: O(n), Space: O(n)"
    #     result = []
    #     def dfs(node, level):
    #         if node is None: return
    #         if len(result) == level: result.append([])
    #         result[level].append(node.val)
    #         if node.left: dfs(node.left, level+1)
    #         if node.right: dfs(node.right, level+1)
    #         pass
    #     dfs(root, 0)
    #     return result


root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().levelOrder(root)
assert result == [
  [3],
  [9,20],
  [15,7]
]