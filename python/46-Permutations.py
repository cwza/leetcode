from typing import List

'''
   0     1     2
  . .   . .   . .
  1 2   0 2   0 1
  . .   . .   . .
  2 1   2 0   1 0
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        "dfs, Time: O(n!)"
        n = len(nums)
        result = []
        done = set()
        def helper(path):
            if len(path) == n:
                result.append(path[:])
                return
            for i, num in enumerate(nums):
                if i not in done:
                    done.add(i)
                    path.append(num)
                    helper(path)
                    done.remove(i)
                    path.remove(num)
        helper([])
        return result

nums = [1, 2, 3]
result = Solution().permute(nums)
print(result) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]