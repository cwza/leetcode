from typing import List
from functools import lru_cache

'''
total = sum(nums)
if total is odd then return False
if total is even:
    target = total // 2
    *** This problem becomes: Can we use nums to build target???***

This problem becomes a Knapsack problem, we can solve it by DP.
Consider take or not take the ith item.
dp[i, val]: Can we use nums[0, i] to build val??
              not take i          take i
dp[i, val] = dp[i-1, val] or dp[i-1, nums[i]-val]
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        "Top-Down with Memoization, Time: O(mn), Space: O(mn)"
        @lru_cache(None)
        def helper(i, val):
            if nums[i] == val: return True
            if val == 0: return False
            if i == 0: return nums[0] == val
            return helper(i-1, val) or ( val > nums[i] and helper(i-1, val-nums[i]) )

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        return helper(len(nums)-1, target)
    def canPartition(self, nums: List[int]) -> bool:
        "Down-Top DP, Time: O(mn), Space: O(mn)"
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [[False]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            for val in range(target+1):
                if nums[i] == val:
                    dp[i][val] = True
                if val == 0:
                    dp[i][val] = False
                if i == 0:
                    dp[i][val] = (nums[0]==val)
                else:
                    dp[i][val] = dp[i-1][val] or (val > nums[i] and dp[i-1][val-nums[i]])
        return dp[len(nums)-1][target]
    def canPartition(self, nums: List[int]) -> bool:
        "DFS+Memoization"
        "Generate all subsets, check if any can form target, use memoization to speedup"
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        @lru_cache(None)
        def dfs(i, total):
            if total > target: return False
            if total == target: return True
            for j in range(i+1, n):
                if dfs(j, total+nums[j]):
                    return True
            return False
        return dfs(-1, 0)

nums = [1,3,2]
result = Solution().canPartition(nums)
assert result == True

nums = [1,5,11,5]
result = Solution().canPartition(nums)
assert result == True

nums = [1,2,3,5]
result = Solution().canPartition(nums)
assert result == False
