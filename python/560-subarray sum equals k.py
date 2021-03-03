from typing import List

'''
k = 7
              0   1   2   3   4   5   6   7
nums=         3,  4,  7,  2, -3,  1,  4,  2
prefixsum=    3,  7, 14, 16, 13, 14, 18, 20
ans = [3, 4], [7], [7, 2, -3, 1], [1, 4, 2]

Where is [1, 4, 2] come from??
See that prefixsum[7]=20.
And we can find that 20-7=13 appeared at prefixsum[4].
That tell us 3+4+7+2-3+1+4+2=20 and 3+4+7+2-3=13
So 1+4+2=7
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        "Brute Force, Time: O(n^2), Space: O(1), TLE"
        n = len(nums)
        ans = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    ans += 1
        return ans
    def subarraySum(self, nums: List[int], k: int) -> int:
        "Prefix Sum + HashMap, Time: O(n), Space: O(n)"
        "Very tricky please see: https://www.youtube.com/watch?v=HbbYPQc-Oo4"
        from collections import Counter
        prefixsum_counter = Counter()
        total = 0
        ans = 0
        for num in nums:
            total += num
            if total == k: ans += 1
            ans += prefixsum_counter[total-k]
            prefixsum_counter[total] += 1
        return ans


nums = [1,1,1]
k = 2
result = Solution().subarraySum(nums, k)
assert result == 2

nums = [1,2,3]
k = 3
result = Solution().subarraySum(nums, k)
assert result == 2