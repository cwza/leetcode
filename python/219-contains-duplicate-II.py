from typing import List

'''
https://www.youtube.com/watch?v=SFMCxqSeM94
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if num in s:
                return True
            s.add(num)
            if len(s) > k:
                s.remove(nums[i-k])
        return False

nums = [1,2,3,1]
k = 3
result = Solution().containsNearbyDuplicate(nums, k)
assert result == True

nums = [1,0,1,1]
k = 1
result = Solution().containsNearbyDuplicate(nums, k)
assert result == True

nums = [1,2,3,1,2,3]
k = 2
result = Solution().containsNearbyDuplicate(nums, k)
assert result == False