from typing import List

'''
Very tricky
Similar to 442
https://www.youtube.com/watch?v=2QugZILS_Q8
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        "Use the origin array to mimic the hashset behavior, Time: O(n), Space: O(1)"
        if len(nums) == 0: return 1
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in range(n):
            if abs(nums[i]) > n:
                continue
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     "Use HashSet, Time: O(n), Space: O(n)"
    #     n = len(nums)
    #     table = set(nums)
    #     for num in range(1, n+1):
    #         if num not in table:
    #             return num
    #     raise Exception("Suck!!!")

nums = [1,2,0]
result = Solution().firstMissingPositive(nums)
assert result == 3

nums = [3,4,-1,1]
result = Solution().firstMissingPositive(nums)
assert result == 2

nums = [7,8,9,11,12]
result = Solution().firstMissingPositive(nums)
assert result == 1