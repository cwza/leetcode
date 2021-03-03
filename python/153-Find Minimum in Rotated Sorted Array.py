from typing import List

'''
O(n) solution is trivial, but there exists an O(logn) solution which uses binary search.
 2  3  4  5  6  7
------------------
 7 (2) 3  4  5  6
 6  7 (2) 3  4  5
 5  6  7 (2) 3  4
 4  5  6  7 (2) 3
 3  4  5  6  7 (2)
------------------
We observed that:
1. The numbers before minimum (2) is always greater than or equal to nums[0]
2. The numbers after minimum (2) is always less than nums[0]

Obviously we can use binary search:
if arr[m] >= arr[0]: search right, l=m+1
else: search left, r=m

Use binary search template:
g(m) = True if arr[m] < arr[0] else False
That is find an minimal m such that arr[m] < arr[0]

Notice that if nums is not be rotated, we can't use above.
How to check if nums is rotated or not??
By observation, if nums[-1] > nums[0]: not rotated, else: rotated
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        "Binary Search, Time: O(logn), Space: O(1)"
        # If nums is not rotated, just return nums[0]
        n = len(nums)
        if nums[-1] >= nums[0]: return nums[0]

        # Binary Search
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            if nums[m] < nums[0]: r = m
            else: l = m + 1
        if l == n: raise Exception("Suck")
        return nums[l]

nums = [3,4,5,1,2]
result = Solution().findMin(nums)
assert result == 1

nums = [4,5,6,7,0,1,2]
result = Solution().findMin(nums)
assert result == 0

nums = [11,13,15,17]
result = Solution().findMin(nums)
assert result == 11