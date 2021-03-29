
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return head
        m = {}
        cur = head
        newNode = Node(cur.val)
        m[cur] = newNode
        while cur.next:
            newNode.next = Node(cur.next.val)
            m[cur.next] = newNode.next
            cur = cur.next
            newNode = newNode.next
        cur = head
        newNode = m[head]
        while cur:
            if cur.random is None: newNode.random = None
            else: newNode.random = m[cur.random]
            cur = cur.next
            newNode = newNode.next
        return m[head]