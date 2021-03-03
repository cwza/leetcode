from typing import List
from bintree_helper import *

'''
For total recursive approach check this:
https://www.youtube.com/watch?v=o1siL8eKCos
'''

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        "DFS+BFS, Time: O(n), Space: O(n)"
        "Generate graph by DFS, then run BFS"
        from collections import defaultdict, deque
        # Generate Graph
        graph = defaultdict(set)
        def dfs(root, parent):
            if root is None: return
            if parent: graph[root.val].add(parent.val)
            if root.left: 
                graph[root.val].add(root.left.val)
                dfs(root.left, root)
            if root.right:
                graph[root.val].add(root.right.val)
                dfs(root.right, root)
        dfs(root, None)

        # Run BFS
        target = target.val
        q = deque([(target, 0)])
        visited = set()
        result = []
        while q:
            node, dist = q.popleft()
            visited.add(node)
            if dist == K: 
                result.append(node)
                continue
            for adj in graph[node]:
                if adj not in visited:
                    q.append((adj, dist+1))
        return result

root = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
target = root.left # (5)
K = 2
result = Solution().distanceK(root, target, K)
print(result) # [7,4,1]