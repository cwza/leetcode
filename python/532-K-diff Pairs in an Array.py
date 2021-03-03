from typing import List

class Solution:
    # def findPairs(self, nums: List[int], k: int) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(1)"
    #     nums.sort()
    #     n = len(nums)
    #     result = 0
    #     dup_check = set()
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             a, b = nums[i], nums[j]
    #             if b - a == k and (a, b) not in dup_check:
    #                 result += 1
    #                 dup_check.add((a, b))
    #     return result
    # def findPairs(self, nums: List[int], k: int) -> int:
    #     "Sort then 2 pointers, Time: O(nlogn), Space: O(1)"
    #     if len(nums) < 2: return 0
    #     nums.sort()
    #     n = len(nums)
    #     results = set()

    #     i, j = 0, 1
    #     while j < n:
    #         if i == j:
    #             j += 1
    #             continue
    #         a, b = nums[i], nums[j]
    #         diff = b - a
    #         if diff == k:
    #             if (a, b) not in results:
    #                 results.add((a, b))
    #             i += 1
    #             j += 1
    #         elif diff > k:
    #             i += 1
    #         else:
    #             j += 1 
    #     return len(results)
    def findPairs(self, nums: List[int], k: int) -> int:
        "Hashset, Time: O(n), Space: O(n)"
        results = set()
        table = set()
        for num in nums:
            target1 = num + k
            target2 = num - k
            if target1 in table:
                results.add((num, num + k))
            if target2 in table:
                results.add((num - k, num))
            table.add(num)
        # print(results)
        return len(results)


nums = [3,1,4,1,5]
k = 2
result = Solution().findPairs(nums, k)
assert result == 2

nums = [1,2,3,4,5]
k = 1
result = Solution().findPairs(nums, k)
assert result == 4

nums = [1,3,1,5,4]
k = 0
result = Solution().findPairs(nums, k)
assert result == 1

nums = [1,2,4,4,3,3,0,9,2,3]
k = 3
result = Solution().findPairs(nums, k)
assert result == 2

nums = [-1,-2,-3]
k = 1
result = Solution().findPairs(nums, k)
assert result == 2