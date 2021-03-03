from typing import List
from collections import defaultdict, deque

'''
Algorithm:
1. Build group graph
2. Run topo_sort at group level
3. Run topo_sort in each group
4. Note that for group -1 items, we have to create new group for each of them

Ex:
# m = 2
# group = [-1,-1,1,0,0,1,0,-1]
# beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

                 0  1  2  3  4  5  6  7
item_to_group = [C, D, B, A, A, B, A, E]
group_to_item = {A:[3,4,6], B:[2,5], C:[0], D:[1], E:[7]}

               0    1    2    3    4       5    6    7
               C    D    B    A    A       B    A    E
beforItems = [[ ], [6], [5], [6], [3, 6], [ ], [ ], [ ]]
                    A    B    A    A  A
# How to build group_graph? Loop over beforeItems, if item and its dep is not in the same group, add this 2 group into graph edge
group_graph = {A:[D], B:[], C:[], D:[], E:[]}
group_topo = [A, B, D, C, E]

# For each group in group_topo, Run topo_sort in it
Group A:
item_graph = {3:[4], 4:[], 6:[3,4]}
item_topo = [6, 3, 4]
Group B:
item_graph = {2:[], 5:[2]}
item_topo = [5, 2]
Group C:
item_graph = {0:[]}
item_topo = [0]
Group D:
item_graph = {1:[]}
item_topo = [1]
Group E:
item_graph = {7:[]}
item_topo = [7]

Result: [6, 3, 4, 5, 2, 0, 1, 7]
'''

def topo_sort(graph):
    '''
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

        Time: O(V+E), Space: O(V)
    '''
    # Build node_to_indegree
    node_to_indegree = {node: 0 for node in graph.keys()}
    for _, adjs in graph.items():
        for adj in adjs:
            node_to_indegree[adj] += 1
    # Put 0 degree node into queue
    q = deque()
    for node, indegree in node_to_indegree.items():
        if indegree == 0:
            q.append(node)
    # Run BFS Modified Alg.
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Remove the outdegree of node, and maintain indegrees
        for adj in graph[node]:
            node_to_indegree[adj] -= 1
            # Push the indegree 0 nodes into queue
            if node_to_indegree[adj] == 0:
                q.append(adj)
    if len(result) == len(graph): return result # Topo_sort exists
    else: return None # There is a cycle in this graph
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        "2 topological sort, Time: O(m+n+E), Space: O(m+n), E is total edges from group_graph and item_graph"
        # Build item_to_group
        item_to_group = []
        s = ord('A') + m
        for group_num in group:
            if group_num == -1:
                group_name = chr(s)
                item_to_group.append(group_name)
                s += 1
            else:
                group_name = chr(ord('A') + group_num)
                item_to_group.append(group_name)
        # Build group_to_items
        group_to_items = defaultdict(list)
        for item, group_name in enumerate(item_to_group):
            group_to_items[group_name].append(item)
        # Build group_graph
        group_graph = {group_name: set() for group_name in group_to_items.keys()}
        for item, deps in enumerate(beforeItems):
            item_group = item_to_group[item]
            for dep in deps:
                dep_group = item_to_group[dep]
                if item_group != dep_group:
                    group_graph[dep_group] = item_group
        # Get group topo sort
        group_topo = topo_sort(group_graph)
        if group_topo is None: return []
        # Get item topo sort for each group
        result = []
        for group_name in group_topo:
            items = group_to_items[group_name]
            # Build item_graph
            item_graph = {item: set() for item in items}
            for item in items:
                for dep in beforeItems[item]:
                    if dep in items:
                        item_graph[dep].add(item)
            # Get item topo sort
            item_topo = topo_sort(item_graph)
            if item_topo is None: return []
            result += item_topo
        return result

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
result = Solution().sortItems(n, m, group, beforeItems)
print(result) # [6,3,4,1,5,2,0,7]

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
result = Solution().sortItems(n, m, group, beforeItems)
print(result) # []