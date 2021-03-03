from typing import List
import heapq
import random

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        "MinHeap, Time: O(n+klogn), Space: O(n)"
        min_heap = [(x*x+y*y, (x, y)) for x, y in points] # (dist, point)
        heapq.heapify(min_heap) # O(n)
        
        ans = []
        while(K):
            K -= 1
            ans.append(heapq.heappop(min_heap)[1])
        return ans
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        "MaxHeap, Time: O(nlogk), Space: O(k)"
        max_heap = [] # (-dist, point)
        for point in points:
            x, y = point
            heapq.heappush(max_heap, (-(x**2+y**2), point))
            if len(max_heap) > K:
                heapq.heappop(max_heap)
        return [point for _, point in max_heap]
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        "Quick Select, Time: O(n), Space: O(1)"
        dist = lambda point: point[0]*point[0] + point[1]*point[1]
        def partition(data, left, right):
            i = left
            j = right
            while i != j:                  
                while dist(data[j]) > dist(data[left]) and i < j:
                    j -= 1
                while dist(data[i]) <= dist(data[left]) and i < j:
                    i += 1
                if i < j:
                    data[i], data[j] = data[j], data[i] 
            data[left], data[i] = data[i], data[left]
            return i
        def helper(data, left, right, k):
            if left >= right: return

            pivot = random.randint(left, right)
            data[left], data[pivot] = data[pivot], data[left]

            pivot_idx = partition(data, left, right)
            if(pivot_idx == k): return
            elif(pivot_idx > k): helper(data, left, pivot_idx-1, k)
            else: helper(data, pivot_idx+1, right, k)

        helper(points, 0, len(points)-1, K-1)
        return points[:K]

points = [[1,3],[-2,2]]
K = 1
result = Solution().kClosest(points, K)
print(result) # [[-2,2]]

points = [[3,3],[5,-1],[-2,4]]
K = 2
result = Solution().kClosest(points, K)
print(result) # [[3,3],[-2,4]]