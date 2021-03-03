from bintree_helper import *

class Solution:
    def maxDepth(self, root) -> int:
        "Post Order Traversal, Time: O(n), Space: O(n)"
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    def maxDepth(self, root) -> int:
        "DFS, Time: O(n), Space: O(n)"
        if root is None: return 0
        def dfs(node):
            d = 0
            if node.left:
                d = max(d, dfs(node.left))
            if node.right:
                d = max(d, dfs(node.right))
            return d + 1
        return dfs(root)

root = deserialize("[3,9,20,null,null,15,7]")
result = Solution().maxDepth(root)
assert result == 3

root = deserialize("[1,null,2]")
result = Solution().maxDepth(root)
assert result == 2

root = deserialize("[null]")
result = Solution().maxDepth(root)
assert result == 0

root = deserialize("[0]")
result = Solution().maxDepth(root)
assert result == 1

