from typing import List
from functools import lru_cache

'''
Special Case of LeetCode188, just use j = 2
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "DP, Time: O(2n), Space: O(2n)"
        n = len(prices)
        if n == 0 or n == 1: return 0
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                if j == 0 or i == 0: return 0
                return max(dp(i-1, j, 0), dp(i-1, j, 1) + prices[i])
            if k == 1:
                if i == 0: return -prices[0]
                if j == 0: return float("-inf")
                return max(dp(i-1, j, 1), dp(i-1, j-1, 0) - prices[i])
        return dp(n-1, 2, 0)

prices = [3,3,5,0,0,3,1,4]
result = Solution().maxProfit(prices)
assert result == 6

prices = [1,2,3,4,5]
result = Solution().maxProfit(prices)
assert result == 4

prices = [7,6,4,3,1]
result = Solution().maxProfit(prices)
assert result == 0

prices = [1]
result = Solution().maxProfit(prices)
assert result == 0
