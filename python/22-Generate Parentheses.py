from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        "Backtracing, Time: O(2^2n), Space: O(2^2n)"
        result = []
        def dfs(l_count, r_count, path):
            if l_count == n and r_count == n:
                result.append(path)
                return
            # left
            if l_count < n:
                dfs(l_count+1, r_count, path+"(")
            # right
            if l_count > r_count:
                dfs(l_count, r_count+1, path+")")
        dfs(0, 0, "")
        return result

n = 3
result = Solution().generateParenthesis(n)
print(result) # ["((()))","(()())","(())()","()(())","()()()"]

n = 1
result = Solution().generateParenthesis(n)
print(result) # ["()"]