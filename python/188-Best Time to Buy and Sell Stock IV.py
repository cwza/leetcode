from typing import List
from functools import lru_cache

'''
DP
i: from day 0 to day i, j: at most j transactions, k: 1 if has stock at day i else 0
dp[i][j][0]: max profit that use at most j transactions from day 0 to day i and have no stack at day i
dp[i][j][1]: same as above, but have stock at day i
result = dp[n-1][k][0]

Transition Function:
Consider 3 conditions: Do-nothing at day i, Sell at day i, Buy at day i
Do-nothing at day i:
  dp[i][j][0] = dp[i-1][j][0]
  dp[i][j][1] = dp[i-1][j][1]
Sell at day i:
  dp[i][j][0] = dp[i-1][j][1] + prices[i]
Buy at day i:
  dp[i][j][1] = dp[i-1][j-1][0] - prices[i]
So the last function:
  dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
  dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

Base Case:
  dp[i][0][0] = 0
  dp[0][j][0] = 0
  dp[0][j][1] = -prices[0]
  dp[i][0][1] = -inf

Special Case:
if k > n/2: same as infinite k LeetCode122, O(n) to solve it
'''

def inf_k(prices: List[int]) -> int:
    "Greedy, Time: O(n), Space: O(1)"
    n = len(prices)
    if n == 1: return 0

    result = 0
    for i in range(0, n-1):
        if prices[i+1] - prices[i] > 0:
            result += prices[i+1] - prices[i]
    return result

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        "DP, Time: O(2nk), Space: O(2nk)"
        n = len(prices)
        if n == 0 or n == 1: return 0
        if k > n/2: return inf_k(prices)
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                if j == 0 or i == 0: return 0
                return max(dp(i-1, j, 0), dp(i-1, j, 1) + prices[i])
            if k == 1:
                if i == 0: return -prices[0]
                if j == 0: return float("-inf")
                return max(dp(i-1, j, 1), dp(i-1, j-1, 0) - prices[i])
        return dp(n-1, k, 0)

k = 2
prices = [2,4,1]
result = Solution().maxProfit(k, prices)
assert result == 2

k = 2
prices = [3,2,6,5,0,3]
result = Solution().maxProfit(k, prices)
assert result == 7
