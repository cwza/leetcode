
class Solution:
    # def tribonacci(self, n: int) -> int:
    #     "DP, Time: O(n), Space: O(n)"
    #     dp = [0] * (n+1)
    #     dp[0], dp[1], dp[2] = 0, 1, 1
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    #     return dp[n]
    def tribonacci(self, n: int) -> int:
        "DP, Time: O(n), Space: O(1)"
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        preprepre, prepre, pre = 0, 1, 1
        cur = 0
        for i in range(3, n+1):
            cur = pre + prepre + preprepre
            preprepre = prepre
            prepre = pre
            pre = cur
        return pre

n = 4
result = Solution().tribonacci(n)
assert result == 4

n = 25
result = Solution().tribonacci(n)
assert result == 1389537