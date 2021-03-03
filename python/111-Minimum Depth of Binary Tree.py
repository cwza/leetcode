from bintree_helper import *

class Solution:
    def minDepth(self, root) -> int:
        "DFS, Time: O(n), Space: O(n)"
        def dfs(node):
            if node is None: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left and node.right: return min(l, r) + 1
            if node.left is None and node.right is None: return 1
            return max(l, r) + 1
        return dfs(root)
    def minDepth(self, root) -> int:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return 0
        q = deque([root])
        level = 1
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return level
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return -1

root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().minDepth(root)
assert result == 2

root = deserialize("[2,null,3,null,4,null,5,null,6]")
result = Solution().minDepth(root)
assert result == 5