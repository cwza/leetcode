from typing import List

class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     "Sort, Time: O(nlogn), Space: O(1)"
    #     if len(nums) == 0: return 0
    #     nums.sort()
    #     result, cur = 1, 1
    #     for i in range(len(nums)-1):
    #         if nums[i+1] == nums[i]:
    #             continue
    #         if nums[i+1] - nums[i] == 1:
    #             cur += 1
    #         else: 
    #             cur = 1
    #         result = max(result, cur)
    #     return result
    def longestConsecutive(self, nums: List[int]) -> int:
        "Hashset, Time: O(n), Space: O(n)"
        table = set(nums)
        result = 0
        for num in nums:
            if num not in table:
                continue
            lower_bound = num - 1
            while lower_bound in table: 
                table.remove(lower_bound)
                lower_bound -= 1
            upper_bound = num + 1
            while upper_bound in table: 
                table.remove(upper_bound)
                upper_bound += 1
            result = max(result, upper_bound - lower_bound - 1)
        return result

nums = [100,4,200,1,3,2]
result = Solution().longestConsecutive(nums)
assert result == 4

nums = [0,3,7,2,5,8,4,6,0,1]
result = Solution().longestConsecutive(nums)
assert result == 9

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
result = Solution().longestConsecutive(nums)
assert result == 7