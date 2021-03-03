from bintree_helper import *

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        "Time: O(n), Space: O(n) for recursive stack"
        result = 0
        def pre_order(root):
            nonlocal result
            if root is None: return
            if low <= root.val <= high:
                result += root.val
            if root.val <= low:
                pre_order(root.right)
            elif root.val >= high:
                pre_order(root.left)
            else:
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        return result

root = deserialize("[10,5,15,3,7,null,18]")
low = 7
high = 15
result = Solution().rangeSumBST(root, low, high)
assert result == 32

root = deserialize("[10,5,15,3,7,13,18,1,null,6]")
low = 6
high = 10
result = Solution().rangeSumBST(root, low, high)
assert result == 23