from typing import List

'''
Ex: [1, 1, 2]

    1     x     2
   . .         . .
  1   2       1   x
  .   .       .
  2   1       1

A key insight to avoid generating any redundant permutation is that at each step rather than viewing each number as a candidate, 
we consider each unique number as the true candidate. 
For instance, at the very beginning, given in the input of [1, 1, 2], we have only two true candidates instead of three.
'''

class Solution:
    # def permuteUnique(self, nums: List[int]):
    #     "Time: O(n!), Space: O(n)"
    #     n = len(nums)
    #     result = set()
    #     done = set()
    #     def helper(path):
    #         if len(path) == n:
    #             result.add(path)
    #             return
    #         for i, num in enumerate(nums):
    #             if i not in done:
    #                 done.add(i)
    #                 helper(path+(num,))
    #                 done.remove(i)
    #     helper(())
    #     return result
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        "Improvement of above, Time: O(n!), Space: O(n)"
        n = len(nums)
        result = []
        done = set()
        def helper(path):
            if len(path) == n:
                result.append(path)
                return
            check_dup = set()
            for i, num in enumerate(nums):
                if i not in done and num not in check_dup:
                    done.add(i)
                    check_dup.add(num)
                    helper(path+[num])
                    done.remove(i)
        helper([])
        return result

nums = [1,1,2]
result = Solution().permuteUnique(nums)
print(result) # [[1,1,2], [1,2,1], [2,1,1]]

nums = [1,2,3]
result = Solution().permuteUnique(nums)
print(result) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]