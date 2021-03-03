from typing import List
from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        "Top-Down with Memoization, Time: O(n^2), Space: O(n), TLE"
        n = len(nums)
        @lru_cache(None)
        def helper(i):
            "True if we can arrive last when we start at i"
            if i == n-1: return True
            if i < 0 or i >=n: return False
            for j in range(1, nums[i]+1):
                if helper(i+j): return True
            return False
        return helper(0)
    def canJump(self, nums: List[int]) -> bool:
        "Down-Top DP, Time: O(n^2), Space: O(n), TLE"
        n = len(nums)
        dp = ["unknown"]*n
        dp[-1] = "True"
        for i in reversed(range(n-1)):
            for j in range(1, nums[i]+1):
                if dp[i+j] == "True":
                    dp[i] = "True"
                    break
            if dp[i] != "True":
                dp[i] = "False"
        return True if dp[0] == "True" else False
    def canJump(self, nums: List[int]) -> bool:
        "Improvement of above, Time: O(n), Space: O(1)"
        "Observation from above: see the break statement, that tell us that we only need the left most True position"
        n = len(nums)
        left_T_pos = n-1
        for i in reversed(range(n-1)):
            if i + nums[i] >= left_T_pos:
                left_T_pos = i
        return left_T_pos == 0

nums = [2,3,1,1,4]
result = Solution().canJump(nums)
assert result == True

nums = [3,2,1,0,4]
result = Solution().canJump(nums)
assert result == False