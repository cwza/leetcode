from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        "DP, Time: O(n), Space: O(n)"
        "dp[i]: max sum of sub-array from 0 to i include i"
        "dp[i] = max(dp[i-1]+nums[i], nums[i])"
        "dp[0] = nums[0]"
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     "DP, Time: O(n), Space: O(1)"
    #     n = len(nums)
    #     pre = nums[0]
    #     cur = 0
    #     result = pre
    #     for i in range(1, n):
    #         cur = max(pre+nums[i], nums[i])
    #         result = max(result, cur)
    #         pre = cur
    #     return result

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = Solution().maxSubArray(nums)
assert result == 6

nums = [1]
result = Solution().maxSubArray(nums)
assert result == 1

nums = [0]
result = Solution().maxSubArray(nums)
assert result == 0

nums = [-1]
result = Solution().maxSubArray(nums)
assert result == -1

nums = [-2147483647]
result = Solution().maxSubArray(nums)
assert result == -2147483647