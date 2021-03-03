from typing import List

class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     "Directly sort, Time: O(nlogn), Space: O(1)"
    #     for i, num in enumerate(nums):
    #         nums[i] = num**2
    #     nums.sort()
    #     return nums
    def sortedSquares(self, nums: List[int]) -> List[int]:
        "Two Pointer, Time: O(n), Space: O(n)"
        "Compare absolute value with two-pointers, then put square value who has the larger absolute value, into result from right to left in descending order."
        result = []
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l]**2 >= nums[r]**2:
                result.append(nums[l]**2)
                l += 1
            else:
                result.append(nums[r]**2)
                r -= 1
        return result[::-1]
nums = [-4,-1,0,3,10]
result = Solution().sortedSquares(nums)
assert result == [0,1,9,16,100]

nums = [-7,-3,2,3,11]
result = Solution().sortedSquares(nums)
assert result == [4,9,9,49,121]
