from typing import List
from bintree_helper import *

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        "BFS with Reverse, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return []
        q = deque([root])
        level = 0
        result = []
        while q:
            sz = len(q)
            result.append([])
            for _ in range(sz):
                node = q.popleft()
                result[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level%2 != 0:
                result[-1] = result[-1][::-1]
            level += 1
        return result
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        "BFS without Reverse, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return []
        q = deque([root])
        level = 0
        result = []
        while q:
            sz = len(q)
            result.append([0]*sz)
            for i in range(sz):
                node = q.popleft()
                if level%2 == 0: idx = i
                else: idx = sz-i-1
                result[-1][idx] = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return result

root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().zigzagLevelOrder(root)
assert result == [[3], [20,9], [15,7]]

