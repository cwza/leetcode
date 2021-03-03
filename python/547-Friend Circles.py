from typing import List, Any, Dict

'''
Algorithm for finding connected component in undirected graph using dfs
https://www.youtube.com/watch?v=9esCn0awd5k
'''

class DisjointSet:
    class Node:
        def __init__(self, data: Any, rank: int):
            self.data = data
            self.rank = rank
            self.parent: "DisjointSet.Node"
    def __init__(self):
        "Space: O(n)"
        self.map: Dict[Any, "DisjointSet.Node"] = {}
    def make_set(self, data: Any):
        node = DisjointSet.Node(data, 0)
        node.parent = node
        self.map[data] = node
    def make_sets(self, datas: List[Any]):
        for data in datas:
            self.make_set(data)
    def union(self, data1: Any, data2: Any) -> bool:
        "Time: O(1)"
        "Combine the 2 sets which contains data1 and data2"
        "If data2 is already in the same set as data1 this function will return False"
        node1, node2 = self.map[data1], self.map[data2]
        parent1, parent2 = self._find(node1), self._find(node2)
        if parent1 == parent2:
            return False
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        return True
    def find_set(self, data: Any) -> "DisjointSet.Node":
        "Time: O(1)"
        "returns the root of sets which include data"
        return self._find(self.map[data]).data
    def _find(self, node: "DisjointSet.Node"):
        parent = node.parent
        if node == parent:
            return parent
        node.parent = self._find(node.parent)
        return node.parent

class Solution:
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     "Undirected Graph Connected Component, Time: O(n^2), Space: O(n)"
    #     visited = set()
    #     def dfs(i):
    #         visited.add(i)
    #         for adj_candidate, is_adj in enumerate(M[i]):
    #             if adj_candidate not in visited and is_adj == 1:
    #                 dfs(adj_candidate)
    #     n = len(M)
    #     result = 0
    #     for i in range(n):
    #         if i in visited:
    #             continue
    #         dfs(i)
    #         result += 1
    #     return result
    def findCircleNum(self, M: List[List[int]]) -> int:
        "Union Find, Time: O(n^2), Space: O(n)"
        n = len(M)
        dst = DisjointSet()
        dst.make_sets([i for i in range(n)])
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    dst.union(i, j)
        circles = set()
        for i in range(n):
            circles.add(dst.find_set(i))
        return len(circles)

M = [[1,1,0],
     [1,1,0],
     [0,0,1]]
result = Solution().findCircleNum(M)
assert result == 2

M = [[1,1,0],
     [1,1,1],
     [0,1,1]]
result = Solution().findCircleNum(M)
assert result == 1

M = [[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]
result = Solution().findCircleNum(M)
assert result == 1