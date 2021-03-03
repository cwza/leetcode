from typing import List
from bintree_helper import *

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        "Recursive, Time: O(n^2), Space: O(n)"
        def helper(i, j):
            if j < i: return None
            max_num = float("-inf")
            max_idx = -1
            for k in range(i, j+1):
                if nums[k] > max_num:
                    max_idx = k
                    max_num = nums[k]
            root = TreeNode(nums[max_idx])
            root.left = helper(i, max_idx-1)
            root.right = helper(max_idx+1, j)
            return root
        root = helper(0, len(nums)-1)
        return root


nums = [3,2,1,6,0,5]
result = Solution().constructMaximumBinaryTree(nums)
drawtree(result)

# nums = [3,2,1]
# result = Solution().constructMaximumBinaryTree(nums)
# drawtree(result)