from linklist_helper import *

class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     "set, Time: O(n), Space: O(n)"
    #     if head is None or head.next is None: return False
    #     check_dup = set()
    #     while head:
    #         if head in check_dup:
    #             return True
    #         else:
    #             check_dup.add(head)
    #             head = head.next
    #     return False
    def hasCycle(self, head: ListNode) -> bool:
        "Slow Fast Pointer, Time: O(n), Space: O(1)"
        if head is None or head.next is None: return False
        slow, fast = head, head
        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
