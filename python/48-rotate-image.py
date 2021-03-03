from typing import List

'''
1. Transpose the matrix
2. reverse each row

ex: 
matrix = [[1,2,3], 
          [4,5,6],
          [7,8,9]]
transpose -> [[1,4,7], 
              [2,5,8],
              [3,6,9]]
reverse each row -> [[7,4,1], 
                     [8,5,2],
                     [9,6,3]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        "Time: O(n^2), Space: O(1)"
        # Transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()


matrix = [[1,2,3], 
          [4,5,6],
          [7,8,9]]
Solution().rotate(matrix)
assert matrix == [[7,4,1],
                  [8,5,2],
                  [9,6,3]]

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
Solution().rotate(matrix)
assert matrix == [[15,13,2,5],
                  [14,3,4,1],
                  [12,6,8,9],
                  [16,7,10,11]]

matrix = [[1]]
Solution().rotate(matrix)
assert matrix == [[1]]

matrix = [[1,2],
          [3,4]]
Solution().rotate(matrix)
assert matrix == [[3,1],
                  [4,2]]