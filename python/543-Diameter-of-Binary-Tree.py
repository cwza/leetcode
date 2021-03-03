from bintree_helper import *

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        "DFS, Time: O(n), Space: O(n)"
        if root is None: return 0
        result = 0
        def depth(node):
            "return the max depth from node to leaf"
            nonlocal result
            ld, rd = 0, 0
            if node.left:
                ld = depth(node.left) + 1
            if node.right:
                rd = depth(node.right) + 1
            result = max(result, ld+rd)
            return max(ld, rd)
        depth(root)
        return result

root = "[1,2,3,4,5,null,null]"
root = deserialize(root)
result = Solution().diameterOfBinaryTree(root)
assert result == 3

root = "[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]"
root = deserialize(root)
result = Solution().diameterOfBinaryTree(root)
assert result == 8