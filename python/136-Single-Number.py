from typing import List
from collections import Counter

'''
* 任何數與0作xor運算結果不變, ex: 3 ^ 0 = 3
* 任何數與自己作xor運算結果為0, ex: 3 ^ 3 = 0
* xor運算有交換律, ex: 1 ^ 2 ^ 3 ^ 4 = 3 ^ 1 ^ 2 ^ 4 = 4 ^ 3 ^ 2 ^ 1
'''

class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     "Hash, time: O(n), space: O(n)"
    #     counter = Counter(nums)
    #     for key, val in counter.items():
    #         if val == 1:
    #             return key
    #     raise Exception("suck!")
    def singleNumber(self, nums: List[int]) -> int:
        "Properties of XOR, time: O(n), space: O(1)"
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [2, 2, 1]
result = Solution().singleNumber(nums)
assert result == 1

nums = [4, 1, 2, 1, 2]
result = Solution().singleNumber(nums)
assert result == 4
