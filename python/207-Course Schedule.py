from typing import List

'''
Does topological sort exists? == Does cycle exists? == Does back edge exists while dfs traversal?
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        "DFS find back edge to detect cycle, Time: O(V+E), Space: O(V)"
        # Generate graph
        graph = [[] for _ in range(numCourses)] 
        for b, a in prerequisites:
            graph[a].append(b)
        # One dfs_visit to detect back edge
        node_state = [0]*numCourses # 0: init, 1: visiting, 2: visited
        def has_cycle(node):
            if node is None: return
            node_state[node] = 1
            for adj in graph[node]:
                if node_state[adj] == 0: 
                    if has_cycle(adj): return True
                elif node_state[adj] == 1: return True
            node_state[node] = 2
            return False
        # Run dfs_visit on all node to detect cycle
        for node in range(numCourses):
            if node_state[node] == 0:
                if has_cycle(node): return False
        return True

numCourses = 2
prerequisites = [[1,0]]
result = Solution().canFinish(numCourses, prerequisites)
assert result == True

numCourses = 2
prerequisites = [[1,0],[0,1]]
result = Solution().canFinish(numCourses, prerequisites)
assert result == False