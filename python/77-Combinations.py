from typing import List


class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     "Time: O(n^k), Space: O(k)"
    #     result = []
    #     def dfs(i, path):
    #         path.append(i)
    #         if len(path) == k:
    #             result.append(path)
    #             return
    #         for j in range(i+1, n+1):
    #             dfs(j, path[:])
    #     for i in range(1, n+1):
    #         dfs(i, [])
    #     return result
    def combine(self, n: int, k: int) -> List[List[int]]:
        "Time: O(n^k), Space: O(k)"
        result = []
        def dfs(i, path):
            if len(path) == k:
                result.append(path)
                return
            for j in range(i+1, n+1):
                dfs(j, path+[j])
        dfs(0, [])
        return result

n = 4
k = 2
result = Solution().combine(n, k)
print(result) # [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]

n = 1
k = 1
result = Solution().combine(n, k)
print(result) # [[1]]

