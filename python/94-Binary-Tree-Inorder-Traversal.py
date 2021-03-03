from typing import List
from bintree_helper import *

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def helper(root):
            if root is None:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        helper(root)
        return result

root = "[1,null,2,3]"
root = deserialize(root)
result = Solution().inorderTraversal(root)
assert result == [1,3,2]

root = "[null]"
root = deserialize(root)
result = Solution().inorderTraversal(root)
assert result == []

root = "[1]"
root = deserialize(root)
result = Solution().inorderTraversal(root)
assert result == [1]

root = "[1,2]"
root = deserialize(root)
result = Solution().inorderTraversal(root)
assert result == [2, 1]

root = "[1,null,2]"
root = deserialize(root)
result = Solution().inorderTraversal(root)
assert result == [1, 2]