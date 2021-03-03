from copy import deepcopy
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # def cloneGraph(self, node: "Node") -> "Node":
    #     return deepcopy(node)
    def cloneGraph(self, node):
        "dfs, Time: O(n)"
        if node is None: return None
        visited = {}
        def helper(node):
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for child in node.neighbors:
                clone.neighbors.append(helper(child))
            return clone
        return helper(node)