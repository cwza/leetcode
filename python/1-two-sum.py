from typing import List
from operator import itemgetter

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     "Brute Force, Time: O(n^2), Space: O(1)"
    #     n = len(nums)
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     "Sort + 2 Pointer, Time: O(nlogn)"
    #     indices, sorted_nums = zip(*sorted(enumerate(nums), key=itemgetter(1)))
    #     i, j = 0, len(nums)-1
    #     while i < j:
    #         if sorted_nums[i] + sorted_nums[j] == target:
    #             return [indices[i], indices[j]]
    #         elif sorted_nums[i] + sorted_nums[j] < target:
    #             i += 1
    #         else:
    #             j -= 1
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     "Two Pass, Time: O(n), Space: O(n)"
    #     table = {num: i for i, num in enumerate(nums)}
    #     for i, num in enumerate(nums):
    #         complement = target - num
    #         if complement in table and i != table[complement]:
    #             return [i, table[complement]]
    #     return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        "One Pass, Time: O(n), Space: O(n)"
        table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            table[num] = i
        return []

nums = [2,7,11,15]
target = 9
result = Solution().twoSum(nums, target)
assert sorted(result) == [0,1]

nums = [3,2,4]
target = 6
result = Solution().twoSum(nums, target)
assert sorted(result) == [1, 2]

nums = [3,3]
target = 6
result = Solution().twoSum(nums, target)
assert sorted(result) == [0, 1]