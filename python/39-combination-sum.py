from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def dfs(i, path, target):
            if target == 0:
                result.append(path[:])
                return
            for j in range(i, n):
                candidate = candidates[j]
                if target-candidate < 0: continue
                path.append(candidate)
                dfs(j, path, target-candidate)
                path.pop()
        dfs(0, [], target)
        return result


candidates = [2,3,6,7]
target = 7
result = Solution().combinationSum(candidates, target)
print(result) # [[7], [2,2,3]]

candidates = [2,3,5]
target = 8
result = Solution().combinationSum(candidates, target)
print(result) # [[2,2,2,2], [2,3,3], [3,5]]