from typing import List
from functools import lru_cache

class Solution:
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     "Brute Force, Time: O(2^n), Space: O(n), TLE"
    #     n = len(nums)
    #     result = 0
    #     def dfs(i, total):
    #         nonlocal result
    #         if i == n:
    #             if total == S:
    #                 result += 1
    #             return
    #         dfs(i+1, total+nums[i])
    #         dfs(i+1, total-nums[i])
    #     dfs(0, 0)
    #     return result
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        "Memoization of above, Timd: O(n*l), Space: O(n*l), l = sum(nums)*2"
        n = len(nums)
        @lru_cache(None)
        def dfs(i, total):
            "returns number of assignments which can add up to S from ith index"
            if i == n:
                if total == S:
                    return 1
                return 0
            return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        return dfs(0, 0)
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     "DP Top-Down, Timd: O(n*l), Space: O(n*l), l = sum(nums)*2"
    #     n = len(nums)
    #     @lru_cache(None)
    #     def helper(i, j):
    #         "returns the number of assignments which can lead to a sum of j upto the ith index"
    #         if i == 0:
    #             return sum([nums[0] == j, -nums[0] == j])
    #         return helper(i-1, j-nums[i]) + helper(i-1, j+nums[i])
    #     return helper(n-1, S)

nums = [1, 1]
S = 0
result = Solution().findTargetSumWays(nums, S)
assert result == 2

nums = [1, 1, 1, 1, 1]
S = 3
result = Solution().findTargetSumWays(nums, S)
assert result == 5