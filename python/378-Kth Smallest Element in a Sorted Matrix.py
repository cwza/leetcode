from typing import List
import heapq

'''
Heap:
https://medium.com/brain-framework/kth-smallest-element-in-sorted-matrix-b20400cf878e

Binary Search:
https://www.cnblogs.com/grandyang/p/5727892.html
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        "MinHeap, Time: O(klogk), Space: O(k)"
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(min(n, k))] # (val, x, y)
        heapq.heapify(pq)
        result = -1
        for _ in range(k):
            result, x, y = heapq.heappop(pq)
            if y+1<n:
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))
        return result
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     "MinHeap, Time: O(klogk), Space: O(k)"
    #     n = len(matrix)
    #     pq = [(matrix[0][0], 0, 0)] # val, x, y 
    #     added = set((0, 0))
    #     result = -1
    #     for _ in range(k):
    #         result, x, y = heapq.heappop(pq)
    #         if 0<=x+1<n and (x+1, y) not in added:
    #             heapq.heappush(pq, (matrix[x+1][y], x+1, y))
    #             added.add((x+1, y))
    #         if 0<=y+1<n and (x, y+1) not in added:
    #             heapq.heappush(pq, (matrix[x][y+1], x, y+1))
    #             added.add((x, y+1))
    #     return result
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     "Binary Search, Time: O(nlogn * logx), Space: O(1), x: max(matrix)-min(matrix)"
    #     def lower_bound(arr, target):
    #         "The first index that its value is greater than target"
    #         "Number of values that less than or equal to target in arr"
    #         l, r = 0, len(arr)
    #         while l < r:
    #             m = l + (r-l)//2
    #             if arr[m] > target : r = m
    #             else: l = m + 1
    #         return l
    #     def g(m):
    #         total = 0 # Number of values that less than or equal to m
    #         for row in matrix: # O(nlogn)
    #             total += lower_bound(row, m)
    #         if total < k: return False
    #         return True
    #     l, r = matrix[0][0], matrix[-1][-1]+1
    #     while l < r:
    #         m = l + (r-l)//2
    #         if g(m): r = m
    #         else: l = m + 1
    #     if l == matrix[-1][-1]+1: raise Exception("Suck")
    #     return l

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
result = Solution().kthSmallest(matrix, k)
assert result == 13

matrix = [[1,3,5],
          [6,7,12],
          [11,14,14]]
k = 6
result = Solution().kthSmallest(matrix, k)
assert result == 11

matrix = [[-5]]
k = 1
result = Solution().kthSmallest(matrix, k)
assert result == -5