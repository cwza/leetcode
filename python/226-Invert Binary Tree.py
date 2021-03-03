from bintree_helper import *

class Solution:
    def invertTree(self, root) -> TreeNode:
        "Time: O(n), Space: O(h)"
        if root is None: return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

root = deserialize("[4,2,7,1,3,6,9]")
result = Solution().invertTree(root)
drawtree(result)