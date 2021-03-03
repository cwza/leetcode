class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        "Recursive1, Time: O(n), Space: O(logn) for recursive stack"
        def dfs(node):
            if node is None: return
            l = node.left
            r = node.right
            while l:
                l.next = r
                l = l.right
                r = r.left
            if node.left:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return root
    def connect(self, root: 'Node') -> 'Node':
        "BFS, Time: O(n), Space: O(logn)"
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
        "Recursive2, Time: O(n), Space: O(logn) for recursive stack"
        "Key: link childs of different tree by parent next link"
        def dfs(root):
            if root is None or root.left is None: return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root
    def connect(self, root: 'Node') -> 'Node':
        "Iterative of recursive2, Time: O(n), Space: O(1)"
        "https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37472/A-simple-accepted-solution"
        ori_root = root
        while root and root.left:
            cur = root
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            root = root.left
        return ori_root