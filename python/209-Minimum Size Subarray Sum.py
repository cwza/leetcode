from typing import List

class Solution:
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(1), TLE"
    #     n = len(nums)
    #     result = float("+inf")
    #     for i in range(n):
    #         total = 0
    #         for j in range(i, n):
    #             total += nums[j]
    #             if total >= s:
    #                 result = min(result, j-i+1)
    #                 break
    #     return result if result != float("+inf") else 0
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        "Binary Search on Window Size, Time: O(nlogn), Space: O(1)"
        n = len(nums)
        if n == 0: return 0
        def g(m): #O(n)
            window_sz = m
            total = sum(nums[:m])
            if total >= s: return True
            for i in range(1, n-window_sz+1):
                total = total - nums[i-1] + nums[i+window_sz-1]
                if total >= s: return True
            return False
        l, r = 1, n+1
        while l < r:
            m = l + (r-l)//2
            if g(m): r = m
            else: l = m + 1
        if l == n+1: return 0
        return l
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        "Sliding Window, Time: O(n), Space: O(1)"
        "https://leetcode.com/problems/minimum-size-subarray-sum/solution/"
        n = len(nums)
        if n == 0: return 0

        l = 0
        total = 0
        result = float("+inf")
        for r in range(n):
            total += nums[r]
            while total >= s:
                result = min(result, r-l+1)
                total -= nums[l]
                l += 1
        return result if result != float("+inf") else 0


s = 7
nums = [2,3,1,2,4,3]
result = Solution().minSubArrayLen(s, nums)
assert result == 2