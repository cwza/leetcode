from typing import List
from math import ceil

'''
The key is to find the boundary of the binary search.
By observation, the boundary can be [1, max(nums)],
Then just do modified binary search
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        "Binary Search, Time: O(nlogm), Space: O(1)"
        "n: len(nums), m: max(nums)"
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r)//2
            val = sum([ceil(num/mid) for num in nums])
            if val > threshold:
                l = mid + 1
            elif val <= threshold:
                r = mid
        return l

nums = [1,2,5,9]
threshold = 6
result = Solution().smallestDivisor(nums, threshold)
assert result == 5

nums = [2,3,5,7,11]
threshold = 11
result = Solution().smallestDivisor(nums, threshold)
assert result == 3

nums = [19]
threshold = 5
result = Solution().smallestDivisor(nums, threshold)
assert result == 4