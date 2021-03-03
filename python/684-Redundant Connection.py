from typing import List, Dict, Any, List
from collections import defaultdict

def has_path(graph, src, dest):
    visited = set()
    def dfs(node):
        visited.add(node)
        if node == dest:
            return True
        for adj in graph[node]:
            if adj not in visited:
                if dfs(adj):
                    return True
        return False
    return dfs(src)

class DisjointSet:
    class Node:
        def __init__(self, data: Any, rank: int):
            self.data = data
            self.rank = rank
            self.parent: "DisjointSet.Node"
    def __init__(self):
        self.map: Dict[Any, "DisjointSet.Node"] = {}
    def make_set(self, data: Any):
        node = DisjointSet.Node(data, 0)
        node.parent = node
        self.map[data] = node
    def make_sets(self, datas: List[Any]):
        for data in datas:
            self.make_set(data)
    def union(self, data1: Any, data2: Any) -> bool:
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
        return self._find(self.map[data]).data
    def _find(self, node: "DisjointSet.Node"):
        parent = node.parent
        if node == parent:
            return parent
        node.parent = self._find(node.parent)
        return node.parent

class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     "DFS, Time: O(n^2), Space: O(n)"
    #     graph = defaultdict(set)
    #     for edge in edges:
    #         src, dest = edge
    #         if has_path(graph, src, dest):
    #             return edge
    #         graph[src].add(dest)
    #         graph[dest].add(src)
    #     return []
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        "Union Find, Time: O(n), Space: O(n)"
        dst = DisjointSet()
        dst.make_sets([i for i in range(1, len(edges)+1)])
        for edge in edges:
            x, y = edge
            if dst.union(x, y) == False:
                return edge
        return []


edges = [[1,2], [1,3], [2,3]]
result = Solution().findRedundantConnection(edges)
assert result == [2,3]

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
result = Solution().findRedundantConnection(edges)
assert result == [1,4]