from typing import List

'''
For Space: O(1) solution
Use the trick like Leetcode442
Key: 1 ≤ a[i] ≤ n, so we can use array index to mimic our hash table
'''

class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     "Hashset, Time: O(n), Space: O(n)"
    #     s = set(nums)
    #     result = []
    #     for num in range(1, len(nums)+1):
    #         if num not in s:
    #             result.append(num)
    #     return result
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        "Index trick, Time: O(2n), Space: O(1)"
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]
        result = []
        for idx, num in enumerate(nums):
            if num > 0:
                result.append(idx+1)
        return result

nums = [4,3,2,7,8,2,3,1]
result = Solution().findDisappearedNumbers(nums)
assert result == [5, 6]