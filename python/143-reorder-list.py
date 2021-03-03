from linklist_helper import *

'''
Ex1: Even
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None

1. split to two list from middle (LeetCode 876 slow, fast pointer)
    1 -> 2 -> 3 -> 4 -> None
    5 -> 6 -> 7 -> 8 -> None
2. reverse the 2nd list (LeetCode 206)
    1 -> 2 -> 3 -> 4 -> None
    8 -> 7 -> 6 -> 5 -> None
3. merge them
    1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 -> None 


Ex2: Odd
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None

1. split to two list from middle (LeetCode 876 slow, fast pointer)
    1 -> 2 -> 3 -> None
    4 -> 5 -> 6 -> 7 -> None
2. reverse the 2nd list (LeetCode 206)
    1 -> 2 -> 3 -> None
    7 -> 6 -> 5 -> 4 -> None
3. merge them
    1 -> 7 -> 2 -> 6 -> 3 -> 5 -> 4 -> None 
'''

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None: return head
        def split(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return head, slow
        def reverse(head):
            cur = head
            prev = None
            while True:
                nxt = cur.next
                cur.next = prev
                if nxt is None: return cur
                prev = cur
                cur = nxt
        def merge(l, r):
            dummy = ListNode()
            cur = dummy
            while l or r:
                if l:
                    cur.next = l
                    cur = cur.next
                    l = l.next
                if r:
                    cur.next = r
                    cur = cur.next
                    r = r.next
            return dummy.next

        l, r = split(head)
        r = reverse(r)
        return merge(l, r)

head = gen_linklist([1, 2, 3, 4])
result = Solution().reorderList(head)
display_linklist(head)

head = gen_linklist([1, 2, 3, 4, 5])
result = Solution().reorderList(head)
display_linklist(head)