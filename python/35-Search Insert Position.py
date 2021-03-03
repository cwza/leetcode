from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        "Binary Search, Time: O(logn), Space: O(1)"
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target: r = m
            else: l = m + 1
        return l

nums = [1,3,5,6]
target = 5
result = Solution().searchInsert(nums, target)
assert result == 2

nums = [1,3,5,6]
target = 2
result = Solution().searchInsert(nums, target)
assert result == 1

nums = [1,3,5,6]
target = 7
result = Solution().searchInsert(nums, target)
assert result == 4

nums = [1,3,5,6]
target = 0
result = Solution().searchInsert(nums, target)
assert result == 0

nums = [1]
target = 0
result = Solution().searchInsert(nums, target)
assert result == 0