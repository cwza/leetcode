from bintree_helper import *

class Solution:
    # def hasPathSum(self, root, sum: int) -> bool:
    #     "DFS, Time: O(n), Space: O(n)"
    #     if root is None: return False
    #     result = False
    #     def dfs(node, total):
    #         nonlocal result
    #         if result:
    #             return
    #         total += node.val
    #         if node.left is None and node.right is None:
    #             if total == sum: result = True
    #         if node.left: dfs(node.left, total)
    #         if node.right: dfs(node.right, total)
    #     dfs(root, 0)
    #     return result
    def hasPathSum(self, root, sum: int) -> bool:
        "DFS, Time: O(n), Space: O(n)"
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

root = deserialize("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
result = Solution().hasPathSum(root, 22)
assert result == True