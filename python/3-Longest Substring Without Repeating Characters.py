
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(n)"
    #     n = len(s)
    #     if n == 0: return 0
    #     if n == 1: return 1
    #     result = 1
    #     for i in range(n-1):
    #         dup_chk = set(s[i])
    #         for j in range(i+1, n):
    #             if s[j] in dup_chk:
    #                 result = max(result, j - i)
    #                 break
    #             dup_chk.add(s[j])
    #         result = max(result, j - i)
    #     return result
    def lengthOfLongestSubstring(self, s: str) -> int:
        "Sliding window, Time: O(n), Space: O(n)"
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1

        i, j = 0, 1
        dup_chk = set(s[0])
        result = 1
        while j < n:
            if i == j:
                dup_chk.add(s[i])
                j += 1
                continue
            if s[j] in dup_chk:
                result = max(result, j - i)
                dup_chk.remove(s[i])
                i += 1
            else:
                dup_chk.add(s[j])
                j += 1
        result = max(result, j - i)
        # print(result)
        return result

s = "abcabcbb"
result = Solution().lengthOfLongestSubstring(s)
assert result == 3

s = "bbbbb"
result = Solution().lengthOfLongestSubstring(s)
assert result == 1

s = "pwwkew"
result = Solution().lengthOfLongestSubstring(s)
assert result == 3

s = ""
result = Solution().lengthOfLongestSubstring(s)
assert result == 0

s = "dvdf"
result = Solution().lengthOfLongestSubstring(s)
assert result == 3
