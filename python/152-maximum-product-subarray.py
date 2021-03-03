from typing import List

'''
Extend of 53
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        "DP, Time: O(n), Space: O(n)"
        n = len(nums)
        # max_dp[i] = largest product of contiguous array that from nums[0, i] include ith element.
        max_dp, min_dp = [0]*n, [0]*n
        max_dp[0], min_dp[0] = nums[0], nums[0]
        for i in range(1, n):
            max_dp[i] = max(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
        return max(max_dp)

nums = [2,3,-2,4]
result = Solution().maxProduct(nums)
assert result == 6

nums = [-2, 0, -1]
result = Solution().maxProduct(nums)
assert result == 0