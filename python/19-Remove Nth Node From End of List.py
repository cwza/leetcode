from linklist_helper import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        "Time: O(n), Space: O(1)"
        dummy = ListNode()
        dummy.next = head
        l, r = dummy, dummy
        for _ in range(n+1):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next

head = gen_linklist([1,2,3,4,5])
n = 2
result = Solution().removeNthFromEnd(head, n)
display_linklist(result) # [1,2,3,5]

head = gen_linklist([1])
n = 1
result = Solution().removeNthFromEnd(head, n)
display_linklist(result) # []

head = gen_linklist([1,2])
n = 1
result = Solution().removeNthFromEnd(head, n)
display_linklist(result) # [1]