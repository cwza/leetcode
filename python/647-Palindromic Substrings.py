from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        "Brute Force, Time: O(n^3), Space: O(1)"
        def is_palindrone(i, j):
            return s[i:j+1] == s[i:j+1][::-1]
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                if is_palindrone(i, j):
                    result += 1
        return result
    def countSubstrings(self, s: str) -> int:
        "Top-Down DP for is_palindrone, Time: O(n^2), Space: O(n^2)"
        @lru_cache(None)
        def is_palindrone(i, j):
            if j<=i: return True
            return s[i] == s[j] and is_palindrone(i+1, j-1)
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                if is_palindrone(i, j):
                    result += 1
        return result
    def countSubstrings(self, s: str) -> int:
        "Down-Top DP for is_palindrone, Time: O(n^2), Space: O(n^2)"
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        result = 0
        for i in range(n): # l = 1
            dp[i][i] = True
            result += 1
        for i in range(n-1): # l = 2
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                result += 1
        for l in range(3, n+1): # l = 3 ~ n
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    result += 1
        return result


s = "abc"
result = Solution().countSubstrings(s)
assert result == 3

s = "aaa"
result = Solution().countSubstrings(s)
assert result == 6

s = "aaaaa"
result = Solution().countSubstrings(s)