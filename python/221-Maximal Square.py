from typing import List

'''
https://www.youtube.com/watch?v=vkFUB--OYy0&feature=emb_logo
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        "DP, Time: O(n^2), Space: O(n^2)"
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)] # dp[i][j] = side length of the maximum square whose bottom right corner is the cell with index (i,j)
        max_len = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: dp[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0: dp[i][j] = 0
                    else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 
                max_len = max(max_len, dp[i][j])
        return max_len ** 2

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
result = Solution().maximalSquare(matrix)
assert result == 4

matrix = [["0","1"],
          ["1","0"]]
result = Solution().maximalSquare(matrix)
assert result == 1

matrix = [["0"]]
result = Solution().maximalSquare(matrix)
assert result == 0

matrix = [["1","1"]]
result = Solution().maximalSquare(matrix)
assert result == 1