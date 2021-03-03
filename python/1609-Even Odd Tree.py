from bintree_helper import *
from collections import deque

'''
Level by level traversal using BFS
'''

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        "O(n)"
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            n = len(queue)
            if level % 2 == 0:
                prev_val = float("-inf")
            else:
                prev_val = float("+inf")
            for _ in range(n):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 != 1 or node.val <= prev_val: return False
                else:
                    if node.val % 2 != 0 or node.val >= prev_val: return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev_val = node.val
            level += 1
        return True

root = deserialize("[1,10,4,3,null,7,9,12,8,6,null,null,2]")
result = Solution().isEvenOddTree(root)
assert result == True

root = deserialize("[5,4,2,3,3,7]")
result = Solution().isEvenOddTree(root)
assert result == False

root = deserialize("[5,9,1,3,5,7]")
result = Solution().isEvenOddTree(root)
assert result == False

root = deserialize("[1]")
result = Solution().isEvenOddTree(root)
assert result == True

root = deserialize("[11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]")
result = Solution().isEvenOddTree(root)
assert result == True
