from typing import Optional
from linklist_helper import *

'''
1. Split list to left and right by middle node, we can find middle node by slow fast pointer like Leetcode(876)
2. Recursive call for left and right list to sort them
3. Merge 2 sorted list left and right like Leetcode(21).
'''

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "Time: O(nlogn), Space: O(logn) for recursive stack which depth is logn"
        if head is None or head.next is None: return head
        def split(head):
            slow, fast, prev = head, head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return head, slow
        def merge(l, r):
            dummy = ListNode()
            cur = dummy
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                    cur = cur.next
                else:
                    cur.next = r
                    r = r.next
                    cur = cur.next
            if l is not None: cur.next = l
            if r is not None: cur.next = r
            return dummy.next

        l, r = split(head)
        l = self.sortList(l)
        r = self.sortList(r)
        result = merge(l, r)
        return result

head = gen_linklist([-1,5,3,4,0])
result = Solution().sortList(head)
display_linklist(head) # [-1,0,3,4,5]

head = gen_linklist([])
result = Solution().sortList(head)
display_linklist(head)