from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        "2 pointer, Time: O(n), Space: O(1)"
        if len(nums) == 0: return []
        if len(nums) == 1: return [f'{nums[0]}']
        nums.append(float("-inf"))
        results = []
        i, j = 0, 0
        while j < len(nums) - 1:
            if nums[j+1] - nums[j] == 1:
                j += 1
            else:
                if i == j:
                    results.append(f'{nums[i]}')
                else:
                    results.append(f'{nums[i]}->{nums[j]}')
                j += 1
                i = j
        return results

nums = [0,1,2,4,5,7]
result = Solution().summaryRanges(nums)
assert result == ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
result = Solution().summaryRanges(nums)
assert result == ["0","2->4","6","8->9"]

nums = []
result = Solution().summaryRanges(nums)
assert result == []

nums = [-1]
result = Solution().summaryRanges(nums)
assert result == ["-1"]

nums = [0]
result = Solution().summaryRanges(nums)
assert result == ["0"]