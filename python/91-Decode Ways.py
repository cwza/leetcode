from functools import lru_cache

'''
Very similar to Leetcode139 Word Break, but the range of j is always less than 2.
So the complexity goes from O(n^2) -> O(n)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        "DFS+Memoization"
        n = len(s)
        @lru_cache(None)
        def dfs(i):
            if i == n: return 1
            result = 0
            for j in range(i+1, min(i+3, n+1)):
                if s[i] != '0' and 1<=int(s[i:j])<=26:
                    result += dfs(j)
            return result
        return dfs(0)
    def numDecodings(self, s: str) -> int:
        "DP, Time: O(n), Space: O(n)"
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(max(0, i-2), i):
                if s[j] != '0' and 1<=int(s[j:i])<=26:
                    dp[i] += dp[j]
        return dp[-1]

s = "12"
result = Solution().numDecodings(s)
assert result == 2

s = "226"
result = Solution().numDecodings(s)
assert result == 3

s = "0"
result = Solution().numDecodings(s)
assert result == 0

s = "1"
result = Solution().numDecodings(s)
assert result == 1

s = "2101"
result = Solution().numDecodings(s)
assert result == 1