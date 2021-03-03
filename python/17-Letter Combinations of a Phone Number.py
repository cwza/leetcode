from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        "Backtracking, Time: O(4^n), Space: O(n)"
        if digits == '': return []
        table = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        results = []
        def dfs(i, path):
            if i == len(digits):
                results.append(path)
                return
            candidates = table[digits[i]]
            for candidate in candidates:
                dfs(i+1, path+candidate)
        dfs(0, '')
        return results

digits = "23"
result = Solution().letterCombinations(digits)
print(result) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
result = Solution().letterCombinations(digits)
print(result) # []

digits = "2"
result = Solution().letterCombinations(digits)
print(result) # ["a","b","c"]