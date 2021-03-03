from typing import List

'''
Very tricky for Time: O(n) and Space: O(1) constraints
Key: 1 ≤ a[i] ≤ n, so we can use array index to mimic our hash table
https://www.youtube.com/watch?v=aMsSF1Il3IY
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        "Time: O(n), Space: O(1)"
        result = []
        for num in nums:
            key = abs(num) - 1
            val = abs(num)
            if nums[key] < 0:
                result.append(val)
            else:
                nums[key] = -nums[key]
        return result

nums = [4,3,2,7,8,2,3,1]
result = Solution().findDuplicates(nums)
assert result == [2, 3]