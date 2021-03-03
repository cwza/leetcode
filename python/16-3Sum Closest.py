from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        "2 pointer, Time: O(n^2), Space: O(1)"
        n = len(nums)
        nums.sort()
        min_diff = float("+inf")
        ans = 0
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target: return s
                if abs(s-target) < min_diff:
                    min_diff = abs(s-target)
                    ans = s
                elif s < target: l += 1
                else: r -= 1
        return ans

nums = [-1,2,1,-4]
target = 1
ans = Solution().threeSumClosest(nums, target)
assert ans == 2

nums = [0,1,2]
target = 3
ans = Solution().threeSumClosest(nums, target)
assert ans == 3