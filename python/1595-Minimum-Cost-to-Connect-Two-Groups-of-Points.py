from typing import List
from functools import lru_cache

'''
Hard
https://www.youtube.com/watch?v=VipkbUDUHLQ
DP and Bitmask to represent state
'''

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        right_min = [min(x) for x in zip(*cost)]

        @lru_cache(None)
        def helper(i, bitmask):
            if i == m:
                return sum([right_min[j] for j in range(n) if not(bitmask & 1<<j)])

            result = float('+inf')
            for j in range(n):
                c = cost[i][j] + helper(i+1, bitmask | 1<<j)
                result = min(result, c)
            return result
        return helper(0, 0)


cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
result = Solution().connectTwoGroups(cost)
assert result == 4

cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
result = Solution().connectTwoGroups(cost)
assert result == 10