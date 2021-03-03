from typing import List

'''
DP: O(m*n)
'''
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_table = [[0 for _ in range(n)] for _ in range(m)]
        min_table = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    max_table[i][j] = grid[i][j]
                    min_table[i][j] = grid[i][j]
                elif i == 0:
                    max_table[i][j] = max_table[i][j-1] * grid[i][j]
                    min_table[i][j] = max_table[i][j-1] * grid[i][j]
                elif j == 0:
                    max_table[i][j] = max_table[i-1][j] * grid[i][j]
                    min_table[i][j] = max_table[i-1][j] * grid[i][j]
                else:
                    possibles = [max_table[i-1][j]*grid[i][j], max_table[i][j-1]*grid[i][j], min_table[i-1][j]*grid[i][j], min_table[i][j-1]*grid[i][j]]
                    max_table[i][j] = max(possibles)
                    min_table[i][j] = min(possibles)
        result = max_table[-1][-1]
        if result < 0:
            return -1
        else:
            return result % (10**9 + 7)

grid = [[-1,-2,-3],
        [-2,-3,-3],
        [-3,-3,-2]]
result = Solution().maxProductPath(grid)
assert result == -1

grid = [[1,-2,1],
        [1,-2,1],
        [3,-4,1]]
result = Solution().maxProductPath(grid)
assert result == 8

grid = [[1, 3],
        [0,-4]]
result = Solution().maxProductPath(grid)
assert result == 0

grid = [[ 1, 4,4,0],
        [-2, 0,0,1],
        [1,-1,1,1]]
result = Solution().maxProductPath(grid)
assert result == 2
