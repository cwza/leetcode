from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        "Time: O(mn), Space: O(m+n)"
        m = len(matrix)
        n = len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
Solution().setZeroes(matrix)
assert matrix == [[1,0,1],
                  [0,0,0],
                  [1,0,1]]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
Solution().setZeroes(matrix)
assert matrix == [[0,0,0,0],
                  [0,4,5,0],
                  [0,3,1,0]]