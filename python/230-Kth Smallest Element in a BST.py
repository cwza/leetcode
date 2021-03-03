from bintree_helper import *

'''
For followup:
Use B+ Tree.
'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        "Recursive Inorder-Traversal, Time: O(H+k), Space: O(H)"
        count = 0
        result = 0
        def dfs(node):
            nonlocal count, result
            if node.left: dfs(node.left)
            if count >= k: return
            count += 1
            result = node.val
            if node.right: dfs(node.right)
        dfs(root)
        return result
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        "Iterative Inorder-Traversal, Time: O(H+k), Space: O(H)"
        def helper(node, stack):
            while node:
                stack.append(node)
                node = node.left
        from collections import deque
        stack = deque()
        helper(root, stack)
        result = 0
        while stack and k:
            cur = stack.pop()
            result = cur.val
            k -= 1
            if cur.right: helper(cur.right, stack)
        return result

root = deserialize("[3,1,4,null,2]")
k = 1
result = Solution().kthSmallest(root, k)
assert result == 1

root = deserialize("[5,3,6,2,4,null,null,1]")
k = 3
result = Solution().kthSmallest(root, k)
assert result == 3