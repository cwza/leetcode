from typing import List
from copy import deepcopy

class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     "Time: O(n^2), Space: O(n^2)"
    #     if triangle == [[]]: return 0
    #     dp = deepcopy(triangle)
    #     for i in range(0, len(dp)):
    #         for j in range(0, len(dp[i])):
    #             if i == 0 and j == 0: continue
    #             elif j == 0: dp[i][j] = dp[i-1][j] + triangle[i][j]
    #             elif j == len(dp[i])-1: dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    #             else: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    #     return min(dp[-1])
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     "Time: O(n^2), Space: O(1), inplace"
    #     if triangle == [[]]: return 0
    #     for i in range(0, len(triangle)):
    #         for j in range(0, len(triangle[i])):
    #             if i == 0 and j == 0: continue
    #             elif j == 0: triangle[i][j] = triangle[i-1][j] + triangle[i][j]
    #             elif j == len(triangle[i])-1: triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
    #             else: triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    #     return min(triangle[-1])
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        "Time: O(n^2), Space: O(n)"
        if triangle == [[]]: return 0
        dp_pre = []
        for i in range(0, len(triangle)):
            dp = [0]*len(triangle[i])
            for j in range(0, len(triangle[i])):
                if i == 0 and j == 0: dp[0] = triangle[i][j]
                elif j == 0: dp[j] = dp_pre[j] + triangle[i][j]
                elif j == len(triangle[i])-1: dp[j] = dp_pre[j-1] + triangle[i][j]
                else: dp[j] = min(dp_pre[j-1], dp_pre[j]) + triangle[i][j]
            dp_pre = dp
        return min(dp_pre)

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
'''
triangle = [
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
'''
result = Solution().minimumTotal(triangle)
assert result == 11