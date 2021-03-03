from typing import List
from collections import defaultdict, deque


class Solution:
    # def canReach(self, arr: List[int], start: int) -> bool:
    #     "BFS, Time: O(n), Space: O(n)"
    #     def build_graph(arr):
    #         n = len(arr)
    #         graph = defaultdict(set)
    #         for i, val in enumerate(arr):
    #             l = i - val
    #             if 0 <= l < n: graph[i].add(l)
    #             r = i + val
    #             if 0 <= r < n: graph[i].add(r)
    #         return graph
    #     graph = build_graph(arr)
    #     q = deque([start])
    #     visited = set()
    #     while q:
    #         cur_idx = q.popleft()
    #         visited.add(cur_idx)
    #         if arr[cur_idx] == 0: return True
    #         for adj in graph[cur_idx]:
    #             if adj not in visited:
    #                 q.append(adj)
    #     return False
    def canReach(self, arr: List[int], start: int) -> bool:
        "Little improvement of above"
        "1: Remove the build_graph process because the original arr can be viewed as a graph"
        "2: Use the original array to check visited, use the fact that the array elements are all non-negative numbers, so we can use negative number to mark the index as visited"
        q = deque([start])
        while q:
            cur_idx = q.popleft()
            arr[cur_idx] = -arr[cur_idx] # mark as visited
            if arr[cur_idx] == 0: return True
            for adj in (cur_idx-arr[cur_idx], cur_idx+arr[cur_idx]):
                if 0 <= adj < len(arr) and arr[adj] >= 0:
                    q.append(adj)
        return False

arr = [4,2,3,0,3,1,2]
start = 5
result = Solution().canReach(arr, start)
assert result == True

arr = [4,2,3,0,3,1,2]
start = 0
result = Solution().canReach(arr, start)
assert result == True

arr = [3,0,2,1,2]
start = 2
result = Solution().canReach(arr, start)
assert result == False