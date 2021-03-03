from typing import List

'''
The solution always exists because of this 2 condition:
nums[-1]==nums[n]==-inf and nums[i]!=nums[i+1]
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        "Naive Sequential Search, Time: O(n), Space: O(1)"
        nums = [float("-inf")] + nums + [float("-inf")]
        n = len(nums)
        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1
        return -1
    def findPeakElement(self, nums: List[int]) -> int:
        "Tricky Sequential Search, Time: O(n), Space: O(1)"
        "Use the fact that nums[-1]==nums[n]==-inf and nums[i]!=nums[i+1]"
        "https://leetcode.com/problems/find-peak-element/solution/"
        "This problem becomes find the minimal index that nums[i] > nums[i+1]"
        nums.append(float("-inf"))
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
        return -1
    def findPeakElement(self, nums: List[int]) -> int:
        "Binary Search from above, Time: O(logn), Space: O(1)"
        nums.append(float("-inf"))
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]: r = m
            else: l = m + 1
        if l == len(nums) - 1: raise Exception("Suck")
        return l

nums = [1,2,3,1]
result = Solution().findPeakElement(nums)
assert result == 2

nums = [1,2,1,3,5,6,4]
result = Solution().findPeakElement(nums)
assert result == 1 or result == 5