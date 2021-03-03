from typing import List

'''
https://www.youtube.com/watch?v=SFMCxqSeM94
'''
class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     if len(set(nums)) < len(nums):
    #         return True
    #     return False
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
    
nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))