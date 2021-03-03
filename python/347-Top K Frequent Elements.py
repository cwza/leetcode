from typing import List

'''
1. Build a frequency hash map
2. Push them into MinHeap(Priority Queue), Frequency as priority
   During push if heap size > k, pop the top
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "Use Counter, Time: O(nlogk), Space: O(n)"
        from collections import Counter
        counter = Counter(nums) # O(n)
        return [num for num, _ in counter.most_common(k)] # O(nlogk + n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "HashMap + MinHeap, Time: O(nlogk), Space: O(n)"
        from collections import defaultdict
        counter = defaultdict(lambda: 0)
        for num in nums: # O(n)
            counter[num] += 1
        
        import heapq
        min_heap = []
        for num, count in counter.items(): # O(n)
            heapq.heappush(min_heap, (count, num)) # O(logk)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(logk)
        return [num for _, num in min_heap]
nums = [1,1,1,2,2,3]
k = 2
result = Solution().topKFrequent(nums, k)
print(result) # [1, 2]

nums = [1]
k = 1
result = Solution().topKFrequent(nums, k)
print(result) # [1]