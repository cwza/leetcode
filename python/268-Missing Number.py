from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        "Hashset, Time: O(n), Space: O(n)"
        n = len(nums)
        s = set(nums)
        for i in range(n+1):
            if i not in s:
                return i
        return 0
    # def missingNumber(self, nums: List[int]) -> int:
    #     "Math, Time: O(n), Space: O(1)"
    #     n = len(nums)
    #     expected_sum = n*(n+1) // 2
    #     actual_sum = sum(nums)
    #     return expected_sum - actual_sum

nums = [3,0,1]
result = Solution().missingNumber(nums)
assert result == 2

nums = [0,1]
result = Solution().missingNumber(nums)
assert result == 2

nums = [9,6,4,2,3,5,7,0,1]
result = Solution().missingNumber(nums)
assert result == 8

nums = [0]
result = Solution().missingNumber(nums)
assert result == 1