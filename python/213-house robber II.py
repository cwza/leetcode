from typing import List

'''
Very similar to leetcode 198, just use it twice and return the max one
1. take nums[0], except nums[-1]
2. take nums[-1], except nums[0]
max(leetcode_198(nums[0:-1]), leetcode_198(1:))
'''

def leetcode_198(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    if n == 2: return max(nums[0], nums[1])
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[n-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        "Time: O(2n), Space: O(2n) can be O(1)"
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        return max(leetcode_198(nums[0:-1]), leetcode_198(nums[1:]))

nums = [2,3,2]
result = Solution().rob(nums)
assert result == 3

nums = [1,2,3,1]
result = Solution().rob(nums)
assert result == 4

nums = [0]
result = Solution().rob(nums)
assert result == 0
