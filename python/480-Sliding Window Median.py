from typing import List
from sortedcontainers import SortedList

"Similar to Leetcode295"

def get_median_from_sorted(sorted_nums):
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[(n-1)//2] + sorted_nums[(n-1)//2+1]) / 2
    else:
        median = sorted_nums[(n-1)//2]
    return median

class Solution:
    # def medianSlidingWindow(self, nums, k: int) -> List[float]:
    #     "Brute Force, Time: O(n*klogk), Space: O(k+n)"
    #     n = len(nums)
    #     if n == 0 or k == 0: return []
    #     if n == 1: return nums

    #     results = []
    #     for start in range(0, n-k+1): # n
    #         end = start + k
    #         median = get_median_from_sorted(sorted(nums[start:end])) # sort: klogk
    #         results.append(median)
    #     return results
    def medianSlidingWindow(self, nums, k: int) -> List[float]:
        "Balenced Binary Search Tree, Time: O(klogk + nlogk), Space: O(k+n)"
        n = len(nums)
        if n == 0 or k == 0: return []
        if n == 1: return nums

        sorted_k_nums = SortedList(nums[:k]) # klogk
        results = [get_median_from_sorted(sorted_k_nums)] # 1
        for cur in range(k, n): # n
            sorted_k_nums.remove(nums[cur-k]) # logk
            sorted_k_nums.add(nums[cur]) # logk
            median = get_median_from_sorted(sorted_k_nums) # 1
            results.append(median)
        return results

nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = Solution().medianSlidingWindow(nums, k)
assert result == [1,-1,-1,3,5,6]