from typing import List
from sortedcontainers import SortedList

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     "Brute Force, Time: O(nk), Space: O(1), TLE"
    #     n = len(nums)
    #     result = []
    #     for end in range(k-1, n):
    #         start = end - k + 1
    #         w_nums = nums[start:end+1]
    #         result.append(max(w_nums))
    #     return result
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     "Balanced Binary Search Tree, Time: O(nlogk), Space: O(k)"
    #     n = len(nums)
    #     sorted_list = SortedList(nums[:k])
    #     result = [sorted_list[-1]]
    #     for end in range(k, n):
    #         start = end - k + 1
    #         be_remove = nums[start-1]
    #         sorted_list.remove(be_remove) # O(logk)
    #         be_add = nums[end]
    #         sorted_list.add(be_add) # O(logk)
    #         result.append(sorted_list[-1])
    #     # print(result)
    #     return result
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        " Monotonic Decreasing Deque, Time: O(n), Space: O(k) "
        from collections import deque
        n = len(nums)
        d = deque() # We store idx in deque, the values are decreasing
        ans = []
        for i in range(n):
            while d and nums[d[-1]] <= nums[i]: d.pop() # Maintain the decreasing order
            while d and d[0] <= i-k: d.popleft() # Maintain the window size
            d.append(i)
            if i >= k-1: ans.append(nums[d[0]])
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = Solution().maxSlidingWindow(nums, k)
assert result == [3,3,5,5,6,7]

nums = [1]
k = 1
result = Solution().maxSlidingWindow(nums, k)
assert result == [1]

nums = [1,-1]
k = 1
result = Solution().maxSlidingWindow(nums, k)
assert result == [1, -1]

nums = [9,11]
k = 2
result = Solution().maxSlidingWindow(nums, k)
assert result == [11]

nums = [4,-2]
k = 2
result = Solution().maxSlidingWindow(nums, k)
assert result == [4]

nums = [7,2,4]
k = 2
result = Solution().maxSlidingWindow(nums, k)
assert result == [7,4]