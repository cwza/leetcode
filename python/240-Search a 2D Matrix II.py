from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        "Search from right-up to left-bottom, Time: O(m+n), Space: O(1)"
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while True:
            if i < 0 or i >=m or j < 0 or j >= n: return False
            if matrix[i][j] == target: return True
            elif target > matrix[i][j]: i += 1
            else: j -= 1



matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 5
result = Solution().searchMatrix(matrix, target)
assert result == True

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 20
result = Solution().searchMatrix(matrix, target)
assert result == False
