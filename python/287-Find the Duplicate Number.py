from typing import List

'''
Following methods can't be used because of the follow up limitations
Brute Force: O(n^2) Time
HashSet: O(n) Space
Sorting: Modify nums
Trick use [1, n] : Modify nums
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        "Time: O(n), Space: O(1), But we modify the nums"
        n = len(nums)
        for num in nums:
            key = abs(num)
            val = abs(num)
            if nums[key] < 0:
                return val
            else:
                nums[key] = -nums[key]
        return -1
    # def findDuplicate(self, nums: List[int]) -> int:
    #     "Binary Search, Time: O(nlogn), Space: O(1)"
    #     def g(m):
    #         count = 0 # number of elements in nums that <= m
    #         for num in nums:
    #             if num <= m:
    #                 count += 1
    #         return count > m
    #     n = len(nums)-1
    #     l, r = 1, n+1
    #     while l < r:
    #         m = l + (r-l)//2
    #         if g(m): r = m # O(n)
    #         else: l = m+1
    #     if l == n+1: return -1
    #     return l
    def findDuplicate(self, nums: List[int]) -> int:
        "2 pointer linklist cycle detection, Time: O(n), Space: O(1)"
        "Treat index as node, value as address of next node"
        "There is a duplicate number in array <=> There is a cycle in this linked list"
        "Find duplicate <=> Find the start node of cycle"
        "Same as LeetCode 142"
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while True:
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]

nums = [2,6,4,1,3,1,5]
result = Solution().findDuplicate(nums)
assert result == 1

nums = [1,3,4,2,2]
result = Solution().findDuplicate(nums)
assert result == 2

nums = [3,1,3,4,2]
result = Solution().findDuplicate(nums)
assert result == 3

nums = [1,1]
result = Solution().findDuplicate(nums)
assert result == 1

nums = [1,1,2]
result = Solution().findDuplicate(nums)
assert result == 1