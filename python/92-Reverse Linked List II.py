from linklist_helper import *

'''
Ex: 1 -> 2 -> 3 -> 4 -> 5 -> N, m = 2, n = 4
Expected result: 1 -> 4 -> 3 -> 2 -> 5 -> N

Iterative:
Init:
    Find the m_prev and m_node is trivial, suppose we already find them
    1 -> 2 -> 3 -> 4 -> 5 -> N
    m_prev = 1
    m_node = 2
    prev = None
    cur = m_node = 2

Run following n-m+1 times, that is 4-2+1=3 to reverse m to n and get n_node and n_nxt
After 1st iter:
    1 -> 2
    2 -> N, 3 -> 4 -> 5 -> N
    prev = 2
    cur = 3
After 2nd iter:
    1 -> 2
    3 -> 2 -> N, 4 -> 5 -> N
    prev = 3
    cur = 4
After 3rd iter:
    1 -> 2
    4 -> 3 -> 2 -> N, 5 -> N
    prev = 4
    cur = 5
n_node = prev = 4
n_nxt = cur = 5

Relink node before m and after n:
    m_node.next = n_nxt = 5
    m_prev.next = n_node = 4
    1 -> 4 -> 3 -> 2 -> 5 -> N
'''

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        "Recursive, Time: O(n), Space: O(n)"
        if head is None or head.next is None: return head
        def reverseFirstN(head, n):
            if head is None or head.next is None: return head
            if n == 1: return head
            new_head = reverseFirstN(head.next, n-1)
            nxt = head.next.next
            head.next.next = head
            head.next = nxt
            return new_head
        if m == 1:
            return reverseFirstN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        "Iterative, Time: O(n), Space: O(1)"
        if head is None or head.next is None: return head
        # Find the m_prev(node that just befor m) and m_node
        dummy = ListNode()
        dummy.next = head
        m_prev = dummy
        for _ in range(m-1):
            m_prev = m_prev.next
        m_node = m_prev.next
        # reverse m to n and find n_node and n_nxt(node that just after n)
        prev = None
        cur = m_node
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        n_nxt = cur
        n_node = prev
        # relink node before m and after n
        m_node.next = n_nxt
        m_prev.next = n_node
        return dummy.next


head = gen_linklist([1,2,3,4,5])
result = Solution().reverseBetween(head, 2, 4)
display_linklist(result)
