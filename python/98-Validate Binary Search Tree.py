from bintree_helper import *

'''
"ValidBST <=> Inorder is sorted
'''

class Solution:
    def isValidBST(self, root) -> bool:
        "Recursive In-Order Traversal, Time: O(n), Space: O(n)"
        prev = float("-inf")
        def dfs(root):
            nonlocal prev
            if root.left: 
                if dfs(root.left) == False: return False
            if root.val <= prev: return False
            prev = root.val
            if root.right: 
                if dfs(root.right) == False: return False
            return True
        return dfs(root)
    def isValidBST(self, root) -> bool:
        "Iterative In-Order Traversal, Time: O(n), Space: O(n)"
        from collections import deque
        stack = deque()
        def helper(root):
            while root:
                stack.append(root)
                root = root.left
        helper(root)
        prev = float("-inf")
        while stack:
            node = stack.pop()
            if node.val <= prev: return False
            prev = node.val
            if node.right:
                helper(node.right)
        return True
root = deserialize("[2,1,3]")
result = Solution().isValidBST(root)
assert result == True

root = deserialize("[5,1,4,null,null,3,6]")
result = Solution().isValidBST(root)
assert result == False

root = deserialize("[1,1]")
result = Solution().isValidBST(root)
assert result == False