from typing import List
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        "DFS"
        n = len(nums)
        @lru_cache(None)
        def dfs(total):
            if total > target:
                return 0
            if total == target:
                return 1
            result = 0
            for num in nums:
                result += dfs(total+num)
            return result
        return dfs(0)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        "DP, Time: O(n*target), Space: O(target)"
        dp = [0]*(target+1) # dp[i] = numbers of combinations that can add up to i
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num < 0:
                    continue
                dp[i] += dp[i-num]
        return dp[-1]

nums = [1, 2, 3]
target = 4
result = Solution().combinationSum4(nums, target)
assert result == 7