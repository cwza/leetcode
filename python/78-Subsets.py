from typing import List
'''
Approach 1:
        0              N
     .     .        .     .
    1       N      1       N
   . .     . .    . .     . .
  2   N   2   N  2   N   2   N

Approach 2:
   0      1      2
 .   .    .  
1     2   2
.
2

Approach 3:
Generate binary representation of 0 ~ 7, then generate subsets from them
000, 001, 010, 011, 100, 101, 110, 111
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        "Approach 1"
        n = len(nums)
        result = []
        def dfs(i, path):
            if i == n:
                result.append(path[:])
                return
            path.append(i)
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)
        dfs(0, [])
        return result
    def subsets(self, nums: List[int]) -> List[List[int]]:
        "Approach 2"
        n = len(nums)
        result = []
        def dfs(i, path):
            result.append(path[:])
            if i==n: return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
        dfs(0, [])
        return result
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     "Approach 3"
    #     n = len(nums)
    #     ans = []
    #     for b in range(1<<n): # 0 ~ 2^n-1
    #         path = []
    #         for i in range(n):
    #             if b & 1<<i: # if ith bit is 1
    #                 path.append(nums[i])
    #         ans.append(path)
    #     return ans

nums = [1,2,3]
result = Solution().subsets(nums)
print(result) #[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]]

nums = [0]
result = Solution().subsets(nums)
print(result) #[[], [0]]