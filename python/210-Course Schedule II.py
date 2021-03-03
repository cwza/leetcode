from typing import List

'''
Topological Sort by DFS:
1. Check cycle by finding back edge
2. Run DFS, get the sequence by dfs end timestamp order
3. Reverse the sequence get by 2


Topological Sort by BFS:
https://www.csie.ntu.edu.tw/~sprout/algo2017/ppt_pdf/topological_sort.pdf
Intuition:
1. 找到一個入度為 0 的點 𝑝
2. 把 𝑝 和它的出度都拔掉，形成 𝐺′
3. 遞迴求解 𝐺′ 的 topological order，然後接在 𝑝 後面形成 𝐺 的 topological order
BFS Modified Implementation:
1. 初始將所有入度為 0 的點都推入 queue
2. 從 queue 中取出元素 p
3. 將 𝑝 的出度都移除掉，並維護各個點的入度值
4. 如果某點在上步驟執行後入度變為 0，則將該點推入 queue
5. 若 queue 不為空，回到步驟 2
6. 當queue為空時，若還有入度非0的點 則該圖不存在拓撲排序(i.e.有環)
7. 否則取出的順序即為拓撲排序
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        "Topological sort by dfs, Time: O(V+E), Space: O(V)"
        # Generate graph
        graph = [[] for _ in range(numCourses)] 
        for b, a in prerequisites:
            graph[a].append(b)

        node_state = [0]*numCourses # 0: init, 1: visiting, 2: visited
        result = []
        def dfs(node):
            "store node into result by dfs end time, and return False if there is a cycle"
            node_state[node] = 1
            for adj in graph[node]:
                if node_state[adj] == 0:
                    if dfs(adj) == False: return False 
                elif node_state[adj] == 1: return False
            node_state[node] = 2
            result.append(node)
            return True
        for node in range(numCourses):
            if node_state[node] == 0:
                if dfs(node) == False: return []
        return result[::-1] # reverse dfs end time order to get topological sort order
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        "Topological sort by bfs, Time: O(V+E), Space: O(V)"
        from collections import deque
        # Generate graph and indegree
        graph = [[] for _ in range(numCourses)] 
        indegree = [0]*numCourses
        for b, a in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        # BFS
        q = deque([node for node in range(numCourses) if indegree[node] == 0]) # Push indegree 0 nodes into queue
        result = []
        while q:
            node = q.popleft() # Remove indegree 0 node
            result.append(node)
            for adj in graph[node]:
                indegree[adj] -= 1 # Update the indegree
                if indegree[adj] == 0: # Push the indegree 0 node into queue
                    q.append(adj)

        if len(result) != numCourses: return [] # has cycle, topological sort does not exists
        return result

numCourses = 2
prerequisites = [[1,0]]
result = Solution().findOrder(numCourses, prerequisites)
print(result) # [0, 1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = Solution().findOrder(numCourses, prerequisites)
print(result) # [0,2,1,3] or [0,1,2,3]

numCourses = 1
prerequisites = []
result = Solution().findOrder(numCourses, prerequisites)
print(result) # [0]