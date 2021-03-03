
from collections import deque

# https://www.cnblogs.com/grandyang/p/5923559.html
class Solution:
    def isLeaf(self, node):
        return node.left is None and node.right is None

    # recursive
    def helper(self, node, is_left):
        if node is None: return 0

        if self.isLeaf(node) and is_left:
            return node.val
        elif self.isLeaf(node) and not is_left:
            return 0
        return self.helper(node.left, True) + self.helper(node.right, False)
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None: return 0

        return self.helper(root.left, True) + self.helper(root.right, False)

    # dfs
    def sumOfLeftLeaves(self, root: TreeNode) -> int: 
        if root is None: return 0

        stack = deque([root])
        result = 0
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None and self.isLeaf(node.left):
                result += node.left.val
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
        return result