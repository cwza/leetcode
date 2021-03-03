from functools import lru_cache

class Solution:
    # def fib(self, N: int) -> int:
    #     "Recursive, time: O(2^N), space: O(2^N)"
    #     def helper(N):
    #         if N == 0: return 0
    #         if N == 1: return 1
    #         return helper(N-1) + helper(N-2)
    #     return helper(N)
    # def fib(self, N: int) -> int:
    #     "Memoization, time: O(n), space: O(n)"
    #     cache = {0: 0, 1: 1}
    #     def helper(N):
    #         if N in cache: return cache[N]
    #         res = helper(N-1) + helper(N-2)
    #         cache[N] = res
    #         return res
    #     return helper(N)
    # def fib(self, N: int) -> int:
    #     "DP, time: O(n), space(n)"
    #     dp = [0]*31
    #     dp[0] = 0
    #     dp[1] = 1
    #     for i in range(2, 31):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[N]
    def fib(self, N: int) -> int:
        "DP, time: O(n), space(1)"
        if N == 0: return 0
        if N == 1: return 1
        tmp1 = 0
        tmp2 = 1
        res = 1
        for i in range(2, N+1):
            res = tmp1 + tmp2
            tmp1, tmp2 = tmp2, res
        return res
    # def fib(self, N: int) -> int:
    #     "Use python lru_cache, time: O(n), space: O(n)"
    #     @lru_cache(None)
    #     def helper(N):
    #         if N == 0: return 0
    #         if N == 1: return 1
    #         return helper(N-1) + helper(N-2)
    #     return helper(N)

N = 2
result = Solution().fib(N)
assert result == 1

N = 4
result = Solution().fib(N)
assert result == 3

N = 10
result = Solution().fib(N)
assert result == 55

N = 30
result = Solution().fib(N)
assert result == 832040