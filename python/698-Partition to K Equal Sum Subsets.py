from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        def dfs(i, groups_total):
            if i == n:
                if all([total == target for total in groups_total]):
                    return True
                else:
                    return False
            for group, total in enumerate(groups_total):
                if total + nums[i] <= target:
                    groups_total[group] += nums[i]
                    if dfs(i+1, groups_total):
                        return True
                    groups_total[group] -= nums[i]
            return False
        nums.sort(reverse=True)
        return dfs(0, [0]*k)

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
result = Solution().canPartitionKSubsets(nums, k)
assert result == True