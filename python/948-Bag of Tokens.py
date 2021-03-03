from typing import List

'''
Greedy
1. sort the list
2. if you have enough power, use the power to get score from left
3. if you don't have enough power, use the scroe to get the power from right
4. be careful that you can't do 3 if your current scroe is less than 1
'''

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        "Greedy, Sort + 2 pointer, Time: O(nlogn), Space: O(1)"
        n = len(tokens)
        if n == 0: return 0
        l, r = 0, n-1
        score = 0
        tokens.sort()
        while l <= r:
            if l == r:
                if P >= tokens[l]: return score + 1
                else: return score
            if P >= tokens[l]:
                score += 1
                P -= tokens[l]
                l += 1
                continue
            else: 
                # tokens[r] + power >= tokens[l], because token[r] >= token[l] and power >= 0
                # so we can assume we always can get the score back next turn
                if score >= 1: # if our score is less than 1, then we can't get any power more
                    score -= 1
                    P += tokens[r]
                    r -= 1
                    continue
                else:
                    return score
        return score

tokens = [100]
P = 50
result = Solution().bagOfTokensScore(tokens, P)
assert result == 0

tokens = [100,200]
P = 150
result = Solution().bagOfTokensScore(tokens, P)
assert result == 1

tokens = [100,200,300,400]
P = 200
result = Solution().bagOfTokensScore(tokens, P)
assert result == 2