from typing import List

'''
ex: [2, 1, 5, 0, 4, 6]
[1, 5, 6] satisfy the problem statement.
How to find it??

Suppose we fix mid=5, how do we know we can form a seq that using 5 as mid and safisfy the problem??
if we know the smallest number from left [2, 1, 5] is 1, the largest number from right [5, 0, 4, 6] is 6
Then we can easily check that 1 < 5 < 6, so we know the answer is True.
We just have to try all number as mid, then check if any of them can form a valid seq.
This method will need O(n^2)

But we can precompute smallest number and largest number!!!
smallest[i] = smallest number from 0 to i (left to right)
largest[i] = largest number from n-1 to i (right to left)
if smallest[mid] < nums[mid] < largest[mid]: return True
Then we reduce the complexity to O(n)
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        "Time: O(n), Space: O(n)"
        n = len(nums)
        if n < 3: return False
        smallest, largest = [0]*n, [0]*n
        smallest[0], largest[-1] = nums[0], nums[-1]
        for i in range(1, n):
            smallest[i] = min(smallest[i-1], nums[i])
        for i in reversed(range(0, n-1)):
            largest[i] = max(largest[i+1], nums[i])
        for mid in range(n):
            if smallest[mid] < nums[mid] < largest[mid]:
                return True
        return False

nums = [1,2,3,4,5]
result = Solution().increasingTriplet(nums)
assert result == True

nums = [5,4,3,2,1]
result = Solution().increasingTriplet(nums)
assert result == False

nums = [2,1,5,0,4,6]
result = Solution().increasingTriplet(nums)
assert result == True