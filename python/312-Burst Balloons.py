from typing import List
from functools import lru_cache

'''
https://www.youtube.com/watch?v=z3hu2Be92UA
dp[i][j]: max coins from nums[i] to nums[j]
Transition Function:
dp[i][j] = max([ dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1], k=[i, j] ])
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        "DP, Time: O(n^3), Space: O(n^2)"
        nums.insert(0, 1)
        nums.append(1)
        @lru_cache(None)
        def helper(i, j):
            if j < i: return 0
            result = 0
            for k in range(i, j+1):
                # If we choose to shoot k last
                result = max(result, helper(i, k-1) + helper(k+1, j) + nums[i-1]*nums[k]*nums[j+1])
            return result
        return helper(1, len(nums)-2)

nums = [3,1,5,8]
result = Solution().maxCoins(nums)
assert result == 167