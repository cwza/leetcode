from typing import List
import heapq

'''
Ex: nums1 = [1, 7, 11], nums2 = [2, 4, 6]
Sum of all pairs matrix:
      2   4    6
    ------------
1  |  3   5    7
7  |  9  11   13
11 | 13  15   17
Find the kth smallest pair, then this problem becomes Leetcode378
Find the kth smallest element in a sorted matrix.
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        "Brute Force + Max Heap, Time: O(k^2*logk), Space: O(k)"
        max_heap = []
        nums1, nums2 = nums1[:k], nums2[:k]
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(max_heap, (-(num1+num2), [num1, num2]))
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        result = []
        while max_heap:
            result.append(heapq.heappop(max_heap)[1])
        return result[::-1]
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        "Use sort fact + Min Heap, Time: O(klogk), Space: O(k)"
        "http://www.noteanddata.com/leetcode-373-Find-K-Pairs-with-Smallest-Sums-weride-interview-problem-java-solution-note.html"
        if len(nums1) == 0 or len(nums2) == 0 or k == 0: return []
        m, n = len(nums1), len(nums2)
        min_heap = [(nums1[i]+nums2[0], i, 0) for i in range(min(m, k))] # sum, x, y
        heapq.heapify(min_heap)
        result = []

        while min_heap and k:
            k -= 1
            _, x, y = heapq.heappop(min_heap)
            result.append([nums1[x], nums2[y]])
            if y+1 < n:
                heapq.heappush(min_heap, (nums1[x]+nums2[y+1], x, y+1))
        return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
result = Solution().kSmallestPairs(nums1, nums2, k)
assert result == [[1,2],[1,4],[1,6]] 

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
result = Solution().kSmallestPairs(nums1, nums2, k)
assert result == [[1,1],[1,1]]

nums1 = [1,2]
nums2 = [3]
k = 3
result = Solution().kSmallestPairs(nums1, nums2, k)
assert result == [[1,3],[2,3]]