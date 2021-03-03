from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        "DP, Time: O(n^2), Space: O(n^2)"
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[0][j] = A[0][j]
        for i in range(1, n):
            for j in range(n):
                if j == 0: dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + A[i][j]
                elif j == n-1: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + A[i][j]
                else: 
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]
        return min(dp[-1])

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result = Solution().minFallingPathSum(A)
assert result == 12