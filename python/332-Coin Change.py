from typing import List

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     "2D-DP, Time: O(nm), Space: O(nm), n=len(coins), m=amount"
    #     n = len(coins)
    #     m = amount+1
    #     dp = [[0]*(m) for _ in range(n)] # dp[i][j] = min number of coins to build j amount money by using coins[0, i]
    #     for i in range(n):
    #         dp[i][0] = 0
    #     for j in range(m):
    #         dp[0][j] = j//coins[0] if j%coins[0]==0 else float("+inf")
    #     for i in range(1, n):
    #         for j in range(1, m):
    #             if j - coins[i] < 0:
    #                 dp[i][j] = dp[i-1][j]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
    #     return dp[-1][-1] if dp[-1][-1] != float("+inf") else -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        "1D-DP, Time: O(nm), Space: O(m), n=len(coins), m=amount"
        n = len(coins)
        m = amount+1
        dp = [float("+inf")]*m # dp[i] = min number of coins to build i
        dp[0] = 0
        for i in range(1, m):
            for x in coins:
                if i - x < 0:
                    continue
                dp[i] = min(dp[i], dp[i-x]+1)
        return dp[-1] if dp[-1] != float("+inf") else -1

coins = [1,2,5]
amount = 11
result = Solution().coinChange(coins, amount)
assert result == 3

coins = [2]
amount = 3
result = Solution().coinChange(coins, amount)
assert result == -1

coins = [1]
amount = 0
result = Solution().coinChange(coins, amount)
assert result == 0

coins = [1]
amount = 1
result = Solution().coinChange(coins, amount)
assert result == 1

coins = [1]
amount = 2
result = Solution().coinChange(coins, amount)
assert result == 2