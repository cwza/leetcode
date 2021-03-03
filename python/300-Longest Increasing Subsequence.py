from typing import List

'''
Solution1 DP:
dp[i]: The LIS length from 0 to i, including i 
Ex:
     [1, 3, 5, 4, 7]
dp = [1, 2, 3, 3, 4] 

Transition function:
dp[i] = max([dp[j]+1 if nums[i]>nums[j]] else 1 for j = 0 ~ i-1)
Initial:
dp[0] = 1
result = max(dp)

Solution2 Patience Sort:
https://www.youtube.com/watch?v=l2rCz7skAlk
'''

class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     "DP, Time: O(n^2), Space: O(n)"
    #     n = len(nums)
    #     if n == 0: return 0
    #     dp = [1] * n
    #     for i in range(1, n):
    #         cur_max = 1
    #         for j in range(0, i):
    #             if nums[i] > nums[j]:
    #                 cur_max = max(cur_max, dp[j]+1)
    #         dp[i] = cur_max
    #     return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        "Patience Sort, Time: O(nlogn), Space: O(n)"
        from bisect import bisect_left
        n = len(nums)
        dp = []
        for num in nums:
            idx = bisect_left(dp, num)
            if idx==len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)

nums = [10,9,2,5,3,7,101,18]
result = Solution().lengthOfLIS(nums)
assert result == 4