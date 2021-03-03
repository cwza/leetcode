from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        n = len(candidates)
        candidates.sort()
        ans = []
        def dfs(i, path, target):
            if target == 0:
                ans.append(path[:])
                return
            check_dup = set()
            for j in range(i, n):
                candidate = candidates[j]
                if target-candidate < 0 or candidate in check_dup: continue
                check_dup.add(candidate)
                path.append(candidate)
                dfs(j+1, path, target-candidate)
                path.pop()
        dfs(0, [], target)
        return ans

candidates = [10,1,2,7,6,1,5]
target = 8
result = Solution().combinationSum2(candidates, target)
print(result) # [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]

candidates = [2,5,2,1,2]
target = 5
result = Solution().combinationSum2(candidates, target)
print(result) # [[1, 2, 2], [5]]

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
result = Solution().combinationSum2(candidates, target)
print(result) # []