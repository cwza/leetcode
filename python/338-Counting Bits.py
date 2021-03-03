from typing import List
from math import floor, log2

'''
       0   1       2             4                               8
num = [0, |1|, |2, 3|, |4, 5, 6, 7|, |8, 9, 10, 11, 12, 13, 14, 15|]
dp  = [0, |1|, |1, 2|, |1, 2, 2, 3|, |1, 2,  2,  3,  2,  3,  3,  4|]
dp[i] = dp[i-2^(floor(lgi))] + 1
dp[0] = 0
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        "DP, Time: O(n), Space: O(n)"
        dp = [0] * (num+1)
        dp[0] = 0
        for i in range(1, num+1):
            dp[i] = dp[i-2**floor(log2(i))] + 1
        return dp
    def countBits(self, num: int) -> List[int]:
        "Without build in log2"
        dp = [0] * (num+1)
        dp[0] = 0
        for i in range(1, num+1):
            tmp = i
            j = 0
            while tmp >= 2:
                j += 1
                tmp = tmp >> 1
            dp[i] = dp[i-2**j] + 1
        return dp

num = 2
result = Solution().countBits(num)
assert result == [0,1,1]

num = 5
result = Solution().countBits(num)
assert result == [0,1,1,2,1,2]