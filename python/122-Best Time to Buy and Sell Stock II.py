from typing import List

'''
Greedy
Find the consecutive valley and peak, add up their diffs
Ex: [1, 7, 2, 3, 6, 7, 6, 7]
One pass to find (1, 7), (2, 7), (6, 7)
result = (7-1) + (7-2) + (7-6)
Note that for (2, 7), we can use (2, 3), (3, 6), (6, 7)
7-2 = (3-2) + (6-3) + (7-6)
'''

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     i = 0
    #     maxprofit = 0
    #     while i < n - 1:
    #         while i < n - 1 and prices[i] >= prices[i + 1]:
    #             i += 1
    #         valley = prices[i]
    #         while i < n - 1 and prices[i] <= prices[i + 1]:
    #             i += 1
    #         peak = prices[i]
    #         maxprofit += peak - valley
    #     return maxprofit
    def maxProfit(self, prices: List[int]) -> int:
        "Greedy, Time: O(n), Space: O(1)"
        n = len(prices)
        if n == 1: return 0

        result = 0
        for i in range(0, n-1):
            if prices[i+1] - prices[i] > 0:
                result += prices[i+1] - prices[i]
        return result

prices = [7,1,5,3,6,4]
result = Solution().maxProfit(prices)
assert result == 7

prices = [1,2,3,4,5]
result = Solution().maxProfit(prices)
assert result == 4

prices = [7,6,4,3,1]
result = Solution().maxProfit(prices)
assert result == 0
