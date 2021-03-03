from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_A, num_B = 0, 0
        secret2, guess2 = [], []
        for s, g in zip(secret, guess):
            if s == g: 
                num_A += 1
            else:
                secret2.append(s)
                guess2.append(g)
        counter = Counter(secret2)
        for g in guess2:
            if counter[g] > 0:
                num_B += 1
                counter[g] -= 1

        return f'{num_A}A{num_B}B'

secret = "1807"
guess = "7810"
result = Solution().getHint(secret, guess)
assert result == '1A3B'

secret = "1123"
guess = "0111"
result = Solution().getHint(secret, guess)
assert result == '1A1B'

secret = "11"
guess = "10"
result = Solution().getHint(secret, guess)
assert result == '1A0B'