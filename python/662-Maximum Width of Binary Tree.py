from bintree_helper import *

'''
The idea is to use heap indexing:

        1
   2         3
 4   5     6   7
8 9 x 11  x 13 x 15
Regardless whether these nodes exist:

Always make the id of left child as parent_id * 2;
Always make the id of right child as parent_id * 2 + 1;
'''

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        q = deque([(root, 1)])
        ans = 0
        while q:
            sz = len(q)
            l, r = -1, -1
            for i in range(sz):
                node, idx = q.popleft()
                if i == 0: l = idx
                if i == sz-1: r = idx
                if node.left: q.append((node.left, idx*2))
                if node.right: q.append((node.right, idx*2+1))
            ans = max(ans, r-l+1)
        return ans
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        "DFS, Time: O(n), Space: O(n)"
        ans = 0
        left_idxes = []
        def dfs(root, idx, level):
            nonlocal ans
            if len(left_idxes) == level:
                left_idxes.append(idx)
            ans = max(ans, idx-left_idxes[level]+1)
            if root.left: dfs(root.left, 2*idx, level+1)
            if root.right: dfs(root.right, 2*idx+1, level+1)
        dfs(root, 1, 0)
        return ans

root = deserialize("[1,3,2,5,3,null,9]")
result = Solution().widthOfBinaryTree(root)
assert result == 4

root = deserialize("[1,1,1,1,null,null,1,1,null,null,1]")
result = Solution().widthOfBinaryTree(root)
assert result == 8
