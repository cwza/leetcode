from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        "Backtracking, Time: O(2^n), Space: O(n)"
        result = []
        def dfs(i, path):
            if i == len(S):
                result.append(path)
                return
            if S[i].isalpha():
                dfs(i+1, path+S[i].upper())
                dfs(i+1, path+S[i].lower())
            else:
                dfs(i+1, path+S[i])
        dfs(0, "")
        return result

S = "a1b2"
result = Solution().letterCasePermutation(S)
print(result) # ["a1b2","a1B2","A1b2","A1B2"]

S = "3z4"
result = Solution().letterCasePermutation(S)
print(result) # ["3z4","3Z4"]

S = "12345"
result = Solution().letterCasePermutation(S)
print(result) # ["12345"]

S = "0"
result = Solution().letterCasePermutation(S)
print(result) # ["0"]