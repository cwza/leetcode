from typing import List
from functools import cmp_to_key

'''
https://medium.com/@ChYuan/leetcode-no-179-largest-number-心得-medium-e578b1d9b89e
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        "O(nlogn)"
        def compare(a, b) :
            return int(f'{str(a)}{str(b)}') - int(f'{str(b)}{str(a)}')
        nums.sort(key=cmp_to_key(compare), reverse=True)
        return str(int(''.join([str(num) for num in nums])))

nums = [10,2]
result = Solution().largestNumber(nums)
assert result == "210"

nums = [3,30,34,5,9]
result = Solution().largestNumber(nums)
assert result == "9534330"