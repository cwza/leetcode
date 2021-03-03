from bintree_helper import *

# class BSTIterator:
#     "Use List"
#     def __init__(self, root):
#         "Time: O(n), Space: O(n)"
#         self.list = []
#         self.cur = 0
#         def in_order(node):
#             if node.left: in_order(node.left)
#             self.list.append(node)
#             if node.right: in_order(node.right)
#         in_order(root)
#     def next(self) -> int:
#         "Time: O(1)"
#         result = self.list[self.cur].val
#         self.cur += 1
#         return result
#     def hasNext(self) -> bool:
#         "Time: O(1)"
#         return self.cur < len(self.list)

# class BSTIterator:
#     "Use Generator"
#     def __init__(self, root):
#         "Time: O(1)"
#         self.generator = self.in_order(root)
#         self._next = None
#     def in_order(self, node):
#         if node.left: yield from self.in_order(node.left)
#         yield node
#         if node.right: yield from self.in_order(node.right)
#     def next(self) -> int:
#         "Time: O(1), Space: O(h)"
#         if self._next:
#             result = self._next.val
#             self._next = None
#         else:
#             result = next(self.generator).val
#         return result
#     def hasNext(self) -> bool:
#         "Time: O(1), Space: O(h)"
#         if self._next:
#             return True
#         try:
#             self._next = next(self.generator)
#         except StopIteration:
#             return False
#         return True

from collections import deque
class BSTIterator:
    "In-Order Traversal by Stack"
    def __init__(self, root):
        "Time: O(h), Space: O(h)"
        self.stack = deque()
        self._helper(root)
    def _helper(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def next(self) -> int:
        "Time: O(1), Space: O(h)"
        node = self.stack.pop()
        if node.right:
            self._helper(node.right)
        return node.val
    def hasNext(self) -> bool:
        "Time: O(1)"
        return len(self.stack) > 0
        
bSTIterator = BSTIterator(deserialize("[7,3,15,null,null,9,20]"))
print(bSTIterator.next());    # return 3
print(bSTIterator.next())   # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False
