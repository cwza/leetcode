from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        "MinHeap, Time: O(nlogk), Space: O(k)"
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min(min_heap)
        
nums = [3,2,1,5,6,4]
k = 2
result = Solution().findKthLargest(nums, k)
assert result == 5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
result = Solution().findKthLargest(nums, k)
assert result == 4