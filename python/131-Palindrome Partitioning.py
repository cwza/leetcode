from typing import List
from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        "Backtracking, Time: O(n*2^n), Space: O(n)"
        n = len(s)
        result = []
        def dfs(i, path):
            if i == n:
                result.append(path)
                return
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    dfs(j, path+[s[i:j]])
        dfs(0, [])
        return result
    def partition(self, s: str) -> List[List[str]]:
        "Backtracking + Top-Down DP on is_palindrone, Time: O(n*2^n), Space: O(n)"
        n = len(s)
        result = []
        @lru_cache(None)
        def is_palindrone(i, j):
            if i == j or i == j-1: return True
            return True if s[i] == s[j-1] and is_palindrone(i+1, j-1) else False
        def dfs(i, path):
            if i == n:
                result.append(path)
                return
            for j in range(i+1, n+1):
                if is_palindrone(i, j):
                    dfs(j, path+[s[i:j]])
        dfs(0, [])
        return result

s = "aab"
result = Solution().partition(s)
print(result) # [["a","a","b"],["aa","b"]]

s = "a"
result = Solution().partition(s)
print(result) # [['a']]