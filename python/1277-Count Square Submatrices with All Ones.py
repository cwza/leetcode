from typing import List

class Solution:
    # def countSquares(self, matrix: List[List[int]]) -> int:
    #     "Use Leetcode304, Time: O(mn*min(m,n)), Space: O(mn), TLE"
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     # Build dp
    #     dp = [[0]*n for _ in range(m)] # sum from (0, 0) to (i, j)
    #     dp[0][0] = matrix[0][0]
    #     for j in range(1, n):
    #         dp[0][j] = dp[0][j-1] + matrix[0][j]
    #     for i in range(1, m):
    #         dp[i][0] = dp[i-1][0] + matrix[i][0]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
    #     # Use dp to get sum of any rectangle       
    #     def helper(point1, point2):
    #         row1, col1 = point1
    #         row2, col2 = point2
    #         leftup = dp[row1-1][col1-1] if row1-1>=0 and col1-1 >= 0 else 0
    #         up = dp[row1-1][col2] if row1-1>=0 else 0
    #         left = dp[row2][col1-1] if col1-1>=0 else 0
    #         return dp[row2][col2] - up - left + leftup
    #     # Calculate all 
    #     result = 0
    #     for i in range(m):
    #         for j in range(n):
    #             for k in range(min(m, n)):
    #                 if i+k > m-1 or j+k > n-1: continue
    #                 if helper((i, j), (i+k, j+k)) == (k+1)**2:
    #                     result += 1
    #     return result
    def countSquares(self, matrix: List[List[int]]) -> int:
        "Almost same as Leetcode221, Time: O(mn), Space: O(mn)"
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)] # dp[i][j] = number of squares that right-bottom is (i, j)
        result = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 0: dp[i][j] = 0
                    else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                result += dp[i][j]
        return result

matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
result = Solution().countSquares(matrix)
assert result == 15

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
result = Solution().countSquares(matrix)
assert result == 7