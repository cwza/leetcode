from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        "DP, Time: O(mn), Space: O(1)"
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for j in range(1, n):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j-1]
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]

obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
result = Solution().uniquePathsWithObstacles(obstacleGrid)
assert result == 2