from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        "Binary Search, Time: O(logn), Space: O(1)"
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target: r = m
            else: l = m + 1
        if l == len(nums) or nums[l] != target: return -1
        return l

nums = [-1,0,3,5,9,12]
target = 9
result = Solution().search(nums, target)
assert result == 4

nums = [-1,0,3,5,9,12]
target = 2
result = Solution().search(nums, target)
assert result == -1