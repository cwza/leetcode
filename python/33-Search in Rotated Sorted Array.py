from typing import List

'''
Use the concept from LeetCode 153
if val < nums[0]: val is at Right hand side
else: val is at Left hand side

The different part of this problem is we can't use one g(m). We have 2 condition to consider:
1. If target is on the same side as nums[m], just run normal binary search
    nums[m] > target: search left, else search right
2. If target is on the different side of nums[m], 
    nums[m] is on the Right side: search left, else search right
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        "Binary Search, Time: O(logn), Space: O(1)"
        def get_pos(val):
            "return 'R' if val is on the rhs else 'L' "
            if val < nums[0]: return "R"
            else: return "L"
        target_pos = get_pos(target)
        # Conditinal binary search
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m]==target: return m # Find it
            m_pos = get_pos(nums[m])
            if m_pos == target_pos: # If nums[m] is on the same side as target
                if nums[m] > target: r = m # search left
                else: l = m + 1 # search right
            else: # If nums[m] is on the different side of target
                if m_pos == "R": r = m # search left
                else: l = m + 1 # search right
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
result = Solution().search(nums, target)
assert result == 4

nums = [4,5,6,7,0,1,2]
target = 3
result = Solution().search(nums, target)
assert result == -1

nums = [1]
target = 0
result = Solution().search(nums, target)
assert result == -1