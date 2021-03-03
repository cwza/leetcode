
class Solution:
    def maxPower(self, s: str) -> int:
        "Two Pointers, Time: O(n), Space: O(1)"
        n = len(s)
        if n == 1: return 1
        i, j, result = 0, 1, 0
        while j < n:
            if s[j] != s[i]:
                result = max(result, j-i)
                i = j
            j += 1
        return max(result, j-i)
    # def maxPower(self, s: str) -> int:
    #     from itertools import groupby
    #     return max([len(list(group)) for _, group in groupby(s)])

s = "leetcode"
result = Solution().maxPower(s)
assert result == 2

s = "abbcccddddeeeeedcba"
result = Solution().maxPower(s)
assert result == 5

s = "triplepillooooow"
result = Solution().maxPower(s)
assert result == 5

s = "hooraaaaaaaaaaay"
result = Solution().maxPower(s)
assert result == 11

s = "tourist"
result = Solution().maxPower(s)
assert result == 1