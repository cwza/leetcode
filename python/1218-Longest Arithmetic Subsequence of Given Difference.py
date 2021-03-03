from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        "DP, Time: O(n), Space: O(n)"
        "https://www.youtube.com/watch?v=1THU4Aa9akQ"
        "dp[i] be the maximum length of a subsequence of the given difference whose last element is i"
        dp = {}
        for x in arr:
            if x-difference in dp:
                dp[x] = dp[x-difference] + 1
            else:
                dp[x] = 1
        return max(dp.values())

arr = [1,2,3,4]
difference = 1
result = Solution().longestSubsequence(arr, difference)
assert result == 4

arr = [1,3,5,7]
difference = 1
result = Solution().longestSubsequence(arr, difference)
assert result == 1

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
result = Solution().longestSubsequence(arr, difference)
assert result == 4