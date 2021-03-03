from typing import List
from functools import lru_cache

'''
https://www.youtube.com/watch?v=YxtQUbKbdUs
Be careful that dp[i] is for s[0, i) not include i!!!!!
dp[i]: True if s[0, i) is word breakable, i=[1, len(s))
dp[0]: True, for empty string case

dp[i] == True, if there exists an j= [0, i) such that
1. s[0, j) is word breakable (i.e. dp[j] == True) and
2. s[j, i) is in wordDict

return dp[-1]

ex: leetcode, [leet, code]
         l  e  e  t  c  o  d  e
dp = [T, F, F, F, T, F, F ,F, T]
'''

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        "DFS + Memorization"
        wordDict = set(wordDict)
        n = len(s)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return True
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    if dfs(j): return True
            return False
        return dfs(0)
    def wordBreak(self, s: str, wordDict) -> bool:
        "Down Top DP, Time: O(m + n^2), Space: O(n+m), n: len(s), m: len(wordDict)"
        n = len(s)
        if len(s) == 0: return False
        wordDict = set(wordDict)
        dp = [False]*(n+1) # dp[i]: [0, i)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if (dp[j] and s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[n]

s = "leetcode"
wordDict = ["leet", "code"]
result = Solution().wordBreak(s, wordDict)
assert result == True

s = "applepenapple"
wordDict = ["apple", "pen"]
result = Solution().wordBreak(s, wordDict)
assert result == True


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
result = Solution().wordBreak(s, wordDict)
assert result == False
    