from typing import List

'''
Key: The answer is equal to the centroids of this graph and the number of this tree-like graph is no more than 2.
Q: How to find centroids??
Alg:
1. Find all leaves(outdegree is 1)
2. Remove them from graph
3. Repeat until the nodes in graph is less than or equel to 2
4. Return the remained nodes 

The process is very like the topological sort, but instead of remove indegree 0 nodes we remove outdegree 1 nodes.
For topological sort, refer to Leetcode 210
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        "Brute Force, Time: O(V^2), Space: O(V)"
        '''
            Treat each node as root, calculate their depths, return the minimum roots.
            This method will get TLE
        '''
        # Generate graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def get_height(root, visited):
            visited.add(root)
            height = 0
            for adj in graph[root]:
                if adj not in visited:
                    height = max(height, get_height(adj, visited))
            return height + 1
        min_height = float("+inf")
        heights = [0]*n
        for root in range(n):
            height = get_height(root, set())
            heights[root] = height
            min_height = min(min_height, height)
        return [node for node, height in enumerate(heights) if height==min_height]
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        "BFS, Time: O(V), Space: O(V)"
        from collections import deque
        if n <= 2: return [i for i in range(n)]
        # Generate graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Push all leaves into queue
        q = deque()
        for node in range(n):
            # Leaves are those node that outdegree == 1
            if len(graph[node]) == 1:
                q.append(node)

        # Remove leaves from graph until the number of nodes in graph is less than or equal to 2
        num_remain_node = n
        while num_remain_node > 2:
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                # Remove the edges that point to leaf and add new leaf
                for adj in graph[node]:
                    graph[adj].remove(node)
                    if len(graph[adj]) == 1: # New leaf
                        q.append(adj)
                num_remain_node -= 1 # Remove leaf from graph
        return [node for node in q]

n = 4
edges = [[1,0],[1,2],[1,3]]
result = Solution().findMinHeightTrees(n, edges)
assert result == [1]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
result = Solution().findMinHeightTrees(n, edges)
assert result == [3,4]

n = 1
edges = []
result = Solution().findMinHeightTrees(n, edges)
assert result == [0]

n = 2
edges = [[0,1]]
result = Solution().findMinHeightTrees(n, edges)
assert result == [0, 1]