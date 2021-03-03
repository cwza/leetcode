from bintree_helper import TreeNode, deserialize, drawtree
from collections import deque

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None: return 0
        stack = deque()
        stack.append((root, f'{root.val}'))
        result = 0
        while len(stack) > 0:
            node, binary_str = stack.pop()
            if node.left is None and node.right is None:
                result += int(binary_str, 2)
                continue
            if node.left is not None:
                stack.append((node.left, f'{binary_str}{node.left.val}'))
            if node.right is not None:
                stack.append((node.right, f'{binary_str}{node.right.val}'))
        return result

root = "[1,0,1,0,1,0,1]"
root = deserialize(root)
result = Solution().sumRootToLeaf(root)
assert result == 22

root = "[1,1]"
root = deserialize(root)
result = Solution().sumRootToLeaf(root)
assert result == 3