from typing import List

'''
DP: O(n)
dp[i]: The max profit from day 0 to day i
minimum[i]: The min price from day 0 to day i

Transition Function:
Consider 2 conditions: not sell at ith day or sell at ith day then take the max of them
dp[i] = max(dp[i-1], prices[i] - minimum[i-1])
minimum[i] = min(minimum[i-1], prices[i])

Base Case:
dp[0] = 0
minimum[0] = prices[0]
'''

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(1)"
    #     n = len(prices)
    #     result = 0
    #     for i in range(0, n-1):
    #         for j in range(i+1, n):
    #             result = max(result, prices[j] - prices[i])
    #     return result
    def maxProfit(self, prices: List[int]) -> int:
        "DP, Time: O(n), Space: O(1)"
        n = len(prices)
        if n == 0 or n == 1: return 0

        result = 0
        minimum = prices[0]

        for i in range(1, n):
            price = prices[i]
            result = max(result, price - minimum)
            minimum = min(minimum, price)

        return result

prices = [7,1,5,3,6,4]
result = Solution().maxProfit(prices)
assert result == 5

prices = [7,6,4,3,1]
result = Solution().maxProfit(prices)
assert result == 0
