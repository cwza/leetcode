from typing import List
from bintree_helper import *

class Solution:
    def averageOfLevels(self, root) -> List[float]:
        "DFS, Time: O(n), Space: O(n)"
        if root is None: return [0]
        sums = []
        counts = []
        def dfs(node, level):
            if len(sums) == level: 
                sums.append(0)
                counts.append(0)
            sums[level] += node.val 
            counts[level] += 1
            if node.left: dfs(node.left, level+1)
            if node.right: dfs(node.right, level+1)
        dfs(root, 0)
        return [s/c for s, c in zip(sums, counts)]
    def averageOfLevels(self, root) -> List[float]:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return [0]

        q = deque([root])
        result = []
        while q:
            n = len(q)
            s, count = 0, 0
            for _ in range(n):
                node = q.popleft()
                s += node.val
                count += 1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(s/count)
        return result
root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().averageOfLevels(root)
assert result == [3, 14.5, 11]
