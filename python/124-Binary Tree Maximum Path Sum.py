from bintree_helper import *

'''
Very like Leetcode543
But be careful that the max_left_sum and max_right_sum may be negative.
For this situation, the best path is not include the negative path.
'''

class Solution:
    def maxPathSum(self, root: TreeNode):
        if root is None: return 0
        ans = float("-inf")
        def dfs(root):
            "return the max_sum [root -> leaf] include root"
            nonlocal ans
            l, r = 0, 0
            if root.left:
                # If left or right is negative, the best is not choose them, that is assign them as 0
                l += max(0, dfs(root.left))
            if root.right:
                r += max(0, dfs(root.right))
            ans = max(ans, l+r+root.val)
            return max(l, r) + root.val
        dfs(root)
        return ans
root = "[1,2,3]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == 6

root = "[-10,9,20,null,null,15,7]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == 42

root = "[-3]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == -3

root = "[2,-1]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == 2

root = "[1,-2,3]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == 4

root = "[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]"
root = deserialize(root)
result = Solution().maxPathSum(root)
assert result == 16