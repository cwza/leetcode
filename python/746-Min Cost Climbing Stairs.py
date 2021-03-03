from typing import List

'''
dp[i]: min cost to climb to ith stair
Transition functions:
dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
Initial case:
dp[0] = dp[1] = 0
'''

class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     "DP, Time: O(n), Space: O(n)"
    #     n = len(cost)
    #     dp = [0]*(n+1)
    #     for i in range(2, n+1):
    #         dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    #     return dp[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        "DP, Time: O(n), Space: O(1)"
        n = len(cost)
        prepre = 0
        pre = 0
        cur = 0
        for i in range(2, n+1):
            cur = min(pre+cost[i-1], prepre+cost[i-2])
            prepre = pre
            pre = cur
        return cur

cost = [10, 15, 20]
result = Solution().minCostClimbingStairs(cost)
assert result == 15

cost =  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result = Solution().minCostClimbingStairs(cost)
assert result == 6