
'''
https://www.youtube.com/watch?v=bClIZj66dVE
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sz = len(s)
        for i in range(1, sz//2+1):
            if sz % i == 0:
                count = sz // i
                if s[0:i]*count == s:
                    return True
        return False

s = "abab"
result = Solution().repeatedSubstringPattern(s)
assert result == True

s = "aba"
result = Solution().repeatedSubstringPattern(s)
assert result == False

s = "abcabcabcabc"
result = Solution().repeatedSubstringPattern(s)
assert result == True