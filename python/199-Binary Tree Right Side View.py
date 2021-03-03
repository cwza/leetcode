from typing import List
from bintree_helper import *

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        "BFS, Time: O(n), Space: O(n)"
        if root is None: return []
        from collections import deque
        q = deque([root])
        result = []
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return result
    def rightSideView(self, root: TreeNode) -> List[int]:
        "DFS, Time: O(n), Space: O(n)"
        result = []
        def dfs(root, level):
            if root is None: return
            if len(result) == level:
                result.append(root.val)
            if root.right: dfs(root.right, level+1)
            if root.left: dfs(root.left, level+1)
        dfs(root, 0)
        return result

root = deserialize("[1,2,3,null,5,null,4]")
result = Solution().rightSideView(root)
assert result == [1, 3, 4]