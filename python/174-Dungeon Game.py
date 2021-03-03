from typing import List

'''
https://www.youtube.com/watch?v=h7mrQrpti-k
'''

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        "DP, Time: O(n^2), Space: O(n^2)"
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0]*n for _ in range(m)] # dp[i][j] = min health from i, j to pricess

        dp[m-1][n-1] = 1-dungeon[m-1][n-1] if 1-dungeon[m-1][n-1] > 1 else 1
        for i in reversed(range(0, m-1)):
            dp[i][-1] = dp[i+1][-1] - dungeon[i][-1] if dp[i+1][-1] - dungeon[i][-1] > 1 else 1
        for j in reversed(range(0, n-1)):
            dp[-1][j] = dp[-1][j+1] - dungeon[-1][j] if dp[-1][j+1] - dungeon[-1][j] > 1 else 1
        for i in reversed(range(0, m-1)):
            for j in reversed(range(0, n-1)):
                dp[i][j] = min(dp[i+1][j] - dungeon[i][j], dp[i][j+1] - dungeon[i][j]) if min(dp[i+1][j] - dungeon[i][j], dp[i][j+1] - dungeon[i][j]) > 1 else 1
        return dp[0][0] 


dungeon = [
    [-2,  -3,  3],
    [-5, -10,  1],
    [10,  30, -5]
]
result = Solution().calculateMinimumHP(dungeon)
assert result == 7