
'''
https://www.youtube.com/watch?v=OqXzKsEWM44
DP + Simulation
Time: O(100^2), Space: O(100^2)
Ex: Poured = 4
       4
   1.5   1.5
0.25  0.5  0.25
dp[i][j]: Total amout flow through (i, j) glass

Method 1: dp[i][j] = Pull from dp[i-1][j], dp[i-1][j+1] 
dp[i][j] = max(0, (dp[i-1][j-1]-1)/2) + max(0, (dp[i-1][j]-1)/2)
Be careful for glasses at 2 side

Method 2: Push dp[i][j] to dp[i+1][j], dp[i+1][j+1]
if dp[i][j] > 1:
    dp[i+1][j] += (dp[i][j]-1)/2
    dp[i+1][j+1] += (dp[i][j]-1)/2

Result:
min(1, dp[query_row][query_glass]
'''

class Solution:
    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    #     "Method 1"
    #     dp = [[0.]*100 for _ in range(100)]
    #     dp[0][0] = poured
    #     for i in range(1, query_row+1):
    #         for j in range(i+1):
    #             if j == 0:
    #                 dp[i][j] = max(0, (dp[i-1][j]-1)/2)
    #             if j == i:
    #                 dp[i][j] = max(0, (dp[i-1][j-1]-1)/2)
    #             else:
    #                 dp[i][j] = max(0, (dp[i-1][j]-1)/2) + max(0, (dp[i-1][j-1]-1)/2)
    #     return min(1, dp[query_row][query_glass])
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        "Method 2"
        dp = [[0.]*100 for _ in range(100)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                if dp[i][j] > 1:
                    dp[i+1][j] += (dp[i][j]-1)/2
                    dp[i+1][j+1] += (dp[i][j]-1)/2
        return min(1, dp[query_row][query_glass])

poured = 1
query_row = 1
query_glass = 1
result = Solution().champagneTower(poured, query_row, query_glass)
assert result == 0.

poured = 2
query_row = 1
query_glass = 1
result = Solution().champagneTower(poured, query_row, query_glass)
assert result == 0.5

poured = 100000009
query_row = 33
query_glass = 17
result = Solution().champagneTower(poured, query_row, query_glass)
assert result == 1
