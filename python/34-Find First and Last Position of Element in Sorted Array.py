from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        "2 Binary Search, Time: O(2*logn), Space: O(1)"
        if len(nums) == 0: return [-1, -1]
        def find_left(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == len(nums) or nums[l] != target: return -1
            return l
        def find_right(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] > target: r = m
                else: l = m + 1
            if nums[l-1] != target: return -1
            return l-1

        l = find_left(nums, target)
        if l == -1: return [-1, -1]
        r = find_right(nums, target)
        return [l, r]

nums = [5,7,7,8,8,10]
target = 8
result = Solution().searchRange(nums, target)
assert result == [3, 4]

nums = [5,7,7,8,8,10]
target = 6
result = Solution().searchRange(nums, target)
assert result == [-1, -1]

nums = []
target = 0
result = Solution().searchRange(nums, target)
assert result == [-1, -1]