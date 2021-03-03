class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        if root is None: return root
        q = deque([root])

        while q:
            sz = len(q)
            dummy = Node()
            pre = dummy
            for _ in range(sz):
                node = q.popleft()
                pre.next = node
                pre = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            del dummy
        return root
    def connect(self, root: 'Node') -> 'Node':
        "Iterative, Time: O(n), Space: O(1)"
        "https://www.cnblogs.com/grandyang/p/4290148.html"
        if root is None: return root
        ori_root = root
        dummy = Node()
        cur = dummy

        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
            if root is None:
                root = dummy.next
                dummy.next = None
                cur = dummy
        return ori_root


