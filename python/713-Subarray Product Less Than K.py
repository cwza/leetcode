from typing import List

'''
ans += right - left + 1....

For those who are confused, let's use the example nums = [10,5,2,6]:

If we start at the 0th index, [10], the number of intervals is obviously 1.
If we move to the 1st index, the window is now [10,5]. The new intervals created are [5] and [10,5], so we add 2.
Now, expand the window to the 2nd index: [10,5,2]. The new intervals are [2], [5,2], and [10,5,2], so we add 3.
The pattern should be obvious by now; we add right - left + 1 to the output variable every loop!
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        "Brute Force, Time: O(n^2), Space: O(1)"
        n = len(nums)
        ans = 0
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod >= k: continue
                else: ans += 1
        return ans
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        "Sliding Window, Time: O(n), Space: O(1)"
        if k <= 1: return 0
        n = len(nums)
        l = 0
        prod = 1
        ans = 0
        for r in range(n):
            prod *= nums[r]
            while prod >= k:
                prod /= nums[l]
                l += 1
            ans += r-l+1
        return ans

nums = [10, 5, 2, 6]
k = 100
result = Solution().numSubarrayProductLessThanK(nums, k)
assert result == 8

nums = [1,2,3]
k = 1
result = Solution().numSubarrayProductLessThanK(nums, k)
assert result == 0