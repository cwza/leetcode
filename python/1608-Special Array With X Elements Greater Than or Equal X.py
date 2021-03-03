from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(1, n+1):
            if sum([1 for num in nums if num >= x]) == x:
                return x
        return -1

nums = [3,5]
result = Solution().specialArray(nums)
assert result == 2

nums = [0,0]
result = Solution().specialArray(nums)
assert result == -1

nums = [0,4,3,0,4]
result = Solution().specialArray(nums)
assert result == 3

nums = [3,6,7,7,0]
result = Solution().specialArray(nums)
assert result == -1
        