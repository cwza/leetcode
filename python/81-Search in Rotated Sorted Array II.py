from typing import List

'''
Almost the same as LeetCode 33, but the elements may duplicate....
The problem is that when nums[m] == arr[0] we can't determin nums[m] is at which side...
For example if nums=[2,2,5,6,0,0,2,2], nums[m]=2.

We need to modify our original binary search algorithm.
If nums[m] == nums[0], we can't reduce our problem to half, we need to use sequential search manner:
So the worst case of this algorithm is O(n)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:     
        "Binary Search, Time: Best: O(logn) Worst: O(n), Space: O(1)"
        if len(nums) == 0: return False
        def get_pos(val):
            "return 'R' if val is on the rhs else 'L' "
            if val < nums[0]: return "R"
            else: return "L"
        target_pos = get_pos(target)
        # Conditinal binary search
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m]==target: return True # Find it at m
            if nums[m] == nums[0]: # Can't decide nums[m] is at which side, use sequential search
                if nums[l] != target: l = l + 1 # Only reduce one element
                else: return True # Find it at l
                continue
            m_pos = get_pos(nums[m])
            if m_pos == target_pos: # If nums[m] is on the same side as target
                if nums[m] > target: r = m # search left
                else: l = m + 1 # search right
            else: # If nums[m] is on the different side of target
                if m_pos == "R": r = m # search left
                else: l = m + 1 # search right
        return False

nums = [2,5,6,0,0,1,2]
target = 0
result = Solution().search(nums, target)
assert result == True

nums = [2,5,6,0,0,1,2]
target = 3
result = Solution().search(nums, target)
assert result == False

nums = [1,3,1,1]
target = 3
result = Solution().search(nums, target)
assert result == True

nums = [1,1,3]
target = 3
result = Solution().search(nums, target)
assert result == True