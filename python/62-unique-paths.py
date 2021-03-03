
'''
DP: O(m*n)
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        "DP, Time: O(mn), Space: O(mn)"
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


m = 3
n = 7
result = Solution().uniquePaths(m, n)
assert result == 28

m = 3
n = 2
result = Solution().uniquePaths(m, n)
assert result == 3

m = 7
n = 3
result = Solution().uniquePaths(m, n)
assert result == 28

m = 3
n = 3
result = Solution().uniquePaths(m, n)
assert result == 6