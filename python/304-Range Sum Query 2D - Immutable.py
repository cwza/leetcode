from typing import List

'''
https://www.youtube.com/watch?v=MSNSqU3BnXk&feature=emb_logo
'''
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         "Time: O(mn), TLE"
#         result = 0
#         for i in range(row1, row2+1):
#             for j in range(col1, col2+1):
#                 result += self.matrix[i][j]
#         return result
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        "Time: O(n^2), Space: O(n^2)"
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)] # dp[i][j] = sum from (0, 0) to (i, j)
        dp[0][0] = matrix[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        self.dp = dp
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        "Time: O(1)"
        if self.dp is None: return 0
        dp = self.dp
        leftup = dp[row1-1][col1-1] if row1-1>=0 and col1-1 >= 0 else 0
        up = dp[row1-1][col2] if row1-1>=0 else 0
        left = dp[row2][col1-1] if col1-1>=0 else 0
        return dp[row2][col2] - up - left + leftup

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
assert numMatrix.sumRegion(2, 1, 4, 3) == 8
assert numMatrix.sumRegion(1, 1, 2, 2) == 11
assert numMatrix.sumRegion(1, 2, 2, 4) == 12

matrix = [[-1]]
numMatrix = NumMatrix(matrix)
assert numMatrix.sumRegion(0, 0, 0, 0) == -1