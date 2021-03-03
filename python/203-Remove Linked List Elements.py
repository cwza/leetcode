from linklist_helper import *

class Solution:
    def removeElements(self, head, val: int) -> ListNode:
        "Time: O(n), Space: O(1)"
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

head = gen_linklist([1,2,6,3,4,5,6])
val = 6
result = Solution().removeElements(head, val)
display_linklist(result)

head = gen_linklist([1,1])
val = 1
result = Solution().removeElements(head, val)
display_linklist(result)