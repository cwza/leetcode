from typing import List
        
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(i, path, target):
            if len(path) == k:
                if target == 0: ans.append(path[:])
                return
            for j in range(i, 10):
                if target-j < 0: continue
                path.append(j)
                dfs(j+1, path, target-j)
                path.pop()
        dfs(1, [], n)
        return ans
k = 3
n = 7
result = Solution().combinationSum3(k, n)
print(result) # [[1,2,4]]

k = 3
n = 9
result = Solution().combinationSum3(k, n)
print(result) # [[1,2,6], [1,3,5], [2,3,4]]