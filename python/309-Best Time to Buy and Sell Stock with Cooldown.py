from typing import List

'''
https://www.youtube.com/watch?v=oL6mRyTn56M

rest: rest(cooldown), sold(cooldown)
hold: rest(buy), hold(cooldown)
sold: hold(sell)

rest[i] = max(rest[i-1], sold[i-1]) # max profit if rest or cooldown on ith day
hold[i] = max(hold[i-1], rest[i-1]-prices[i]) # max profit if hold stock on ith day
sold[i] = hold[i-1]+prices[i] # max profit if sold stock on ith day

rest[0] = 0
hold[0] = -prices[0]
sold[0] = -inf
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "DP, Time: O(n), Space: O(n)"
        n = len(prices)
        if n <= 1: return 0

        rest, hold, sold = [0]*n, [0]*n, [0]*n
        rest[0], hold[0], sold[0] = 0, -prices[0], float("-inf")

        for i in range(1, n):
            rest[i] = max(rest[i-1], sold[i-1])
            hold[i] = max(hold[i-1], rest[i-1]-prices[i])
            sold[i] = hold[i-1] + prices[i]
        return max(rest[-1], sold[-1])

prices = [1,2,3,0,2]
result = Solution().maxProfit(prices)
assert result == 3