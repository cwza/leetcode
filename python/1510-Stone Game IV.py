
'''
Hint:
Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.

Transition Function:
dp[i]: True if current player can win if with i remaining stone
bob = [dp[i - x*x] for x in [1, ..., floor(sqrt(n))]]
if any of bob is False: dp[i] = True
else: dp[i] = False

Initial State
dp[0] = False, dp[1] = True, dp[2] = False
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        "dp, Time: O(n * sqrt(n)), Space: O(n)"
        if n == 1: return True
        if n == 2: return False

        dp = [False] * (n+1) # True if current player can win with i remaining stone
        dp[0], dp[1], dp[2] = False, True, False

        for i in range(3, n+1):
            for x in range(1, int(i**0.5)+1): # Try all square number under i
                if dp[i - x*x] == False: # if we can let bob to some state that he must lose, Alice will win
                    dp[i] = True
                    break
        # print(dp)
        return dp[n]

n = 1
result = Solution().winnerSquareGame(n)
assert result == True

n = 2
result = Solution().winnerSquareGame(n)
assert result == False

n = 4
result = Solution().winnerSquareGame(n)
assert result == True

n = 7
result = Solution().winnerSquareGame(n)
assert result == False

n = 17
result = Solution().winnerSquareGame(n)
assert result == False