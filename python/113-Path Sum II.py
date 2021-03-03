from typing import List
from bintree_helper import *

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        "DFS, Time: O(n), Space: O(n)"
        if root is None: return []
        result = []
        def dfs(root, total, path):
            if root.left is None and root.right is None and total == sum:
                result.append(path[:])
            if root.left:
                path.append(root.left.val)
                dfs(root.left, total+root.left.val, path)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, total+root.right.val, path)
                path.pop()
        dfs(root, root.val, [root.val])
        return result
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return []
        q = deque([(root, root.val, [root.val])])
        result = []
        while q:
            node, total, path = q.popleft()
            if node.left is None and node.right is None and total == sum:
                result.append(path)
            if node.left:
                q.append((node.left, total+node.left.val, path+[node.left.val]))
            if node.right:
                q.append((node.right, total+node.right.val, path+[node.right.val]))
        return result



root = deserialize("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
sum = 22
result = Solution().pathSum(root, sum)
print(result) # [[5,4,11,2],[5,8,4,5]]