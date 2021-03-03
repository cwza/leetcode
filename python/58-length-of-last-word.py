
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) == 0: return 0
        return len(words[-1])

s = "Hello World"
result = Solution().lengthOfLastWord(s)
assert result == 5

s = " "
result = Solution().lengthOfLastWord(s)
assert result == 0

s = ""
result = Solution().lengthOfLastWord(s)
assert result == 0
