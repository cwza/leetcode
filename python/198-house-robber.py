from typing import List
from functools import lru_cache

'''
https://medium.com/@desolution/從leetcode學演算法-28-dynamic-programming-6-8e5a81a8437d
dp[i]: max money rob from nums[0] to nums[i]
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        "Down-Top DP, Time: O(n), Space: O(n) can be implemented to O(1)"
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
    # def rob(self, nums: List[int]) -> int:
    #     "Top-Down Memoization, Time: O(n), Space: O(n)"
    #     if len(nums) == 0: return 0
    #     @lru_cache(None)
    #     def helper(i):
    #         if i == 0: return nums[0]
    #         if i == 1: return max(nums[0], nums[1])
    #         return max(helper(i-1), helper(i-2) + nums[i])
    #     return helper(len(nums)-1)

nums = [1,2,3,1]
result = Solution().rob(nums)
assert result == 4

nums = [2,7,9,3,1]
result = Solution().rob(nums)
assert result == 12

nums = [2,1,1,2]
result = Solution().rob(nums)
assert result == 4

nums = []
result = Solution().rob(nums)
assert result == 0