from typing import List
from collections import deque

'''
https://www.youtube.com/watch?v=pqCy9Z4x4qs
Problem:
    i < j < k, nums[i] < nums[k] < nums[j]
'''

class Solution:
    # def find132pattern(self, nums: List[int]) -> bool:
    #     "Brute Force, Time: O(n^3), Space: O(1)"
    #     n = len(nums)
    #     for i in range(n-2):
    #         for j in range(i+1, n-1):
    #             for k in range(j+1, n):
    #                 if nums[i] < nums[k] < nums[j]:
    #                     return True
    #     return False
    # def find132pattern(self, nums: List[int]) -> bool:
    #     "Time: O(n^2), Space: O(1)"
    #     '''
    #         1. Try all j, k st j < k and check nums[j] > nums[k]: O(n^2)
    #         2. So now fix j, k:
    #            Check if we can find an i st i < j and nums[i] < nums[k]
    #            How to find that i in O(1)?? Pre-compute it
    #         3. min_val[x]: min value in nums from 0 to x, one pass to get this array: O(n)
    #            The most possible i that satisfy 2 is min_val[j-1]
    #            So just check if min_val[j-1] < nums[k]
    #     '''
    #     n = len(nums)
    #     if n < 3: return False
    #     # 3
    #     min_val = [nums[0]]
    #     for x in range(1, n):
    #         min_val.append(min(min_val[x-1], nums[x]))
    #     # 1, 2
    #     for j in range(1, n-1):
    #         for k in range(j+1, n):
    #             if nums[j] > nums[k] and min_val[j-1] < nums[k]:
    #                 return True
    #     return False
    def find132pattern(self, nums: List[int]) -> bool:
        "Time: O(n), Space: O(n)"
        '''
            1. This time we just try all j: O(n)
            2. So now fix j:
               Same as above the most possible i should be the min_val[j-1], check this i satisfy nums[i] < nums[j]
            3. Now we want to find what k?
               The most possible k is the max one in [j+1, ..., n-1] which is less than nums[j]
               We need to find this value in O(1) and check if this k satisfy nums[i] < nums[k] < nums[j]
            4. We can use bisect search to find this value in O(logn) and this alg will be O(nlogn)
            5. But we can use stack to achive O(1)!!!
               Key: loop j from right to left, maintain a stack which top is always the max one in [j+1, ..., n-1]
                    if the top is smaller than nums[j] check it and pop it
                    else add nums[j] in stack
        '''
        n = len(nums)
        if n < 3: return False
        # construct min_val
        min_val = [nums[0]]
        for x in range(1, n):
            min_val.append(min(min_val[x-1], nums[x]))
        # loop j from right to left and maintain the stack
        stack = deque()
        for j in reversed(range(1, n)):
            while stack and stack[-1] < nums[j]:
                if min_val[j-1] < stack[-1] < nums[j]:
                    return True
                stack.pop()
            stack.append(nums[j])
        return False

nums = [1,2,3,4]
result = Solution().find132pattern(nums)
assert result == False

nums = [3,1,4,2]
result = Solution().find132pattern(nums)
assert result == True

nums = [-1,3,2,0]
result = Solution().find132pattern(nums)
assert result == True