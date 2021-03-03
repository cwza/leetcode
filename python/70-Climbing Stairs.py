from functools import lru_cache

'''
dp[n]: number of dinstinct ways to climb n stairs
dp[n] = dp[n-1] + dp[n-2]
dp[1] = 1
dp[2] = 2
'''

class Solution:
    # @lru_cache(None)
    # def climbStairs(self, n: int) -> int:
    #     "Top-Down with Memoization, Time: O(n), Space: O(n)"
    #     if n == 1: return 1
    #     if n == 2: return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
    # def climbStairs(self, n: int) -> int:
    #     "Down-Top dp, Time: O(n), Space: O(n) can be reduce to O(1)"
    #     if n == 1: return 1
    #     if n == 2: return 2
    #     dp = [0] * (n+1)
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]
    def climbStairs(self, n: int) -> int:
        "Down-Top dp, Time: O(n), Space: O(1)"
        if n == 1: return 1
        if n == 2: return 2
        pre = 1
        cur = 2
        for i in range(3, n+1):
            cur, pre = cur+pre, cur
        return cur

n = 2
result = Solution().climbStairs(n)
assert result == 2

n = 3
result = Solution().climbStairs(n)
assert result == 3