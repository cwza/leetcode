from linklist_helper import *

class Solution:
    def mergeTwoLists(self, l1, l2):
        "Time: O(n), Space: O(1)"
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next


l1 = gen_linklist([1,2,4])
l2 = gen_linklist([1,3,4])
result = Solution().mergeTwoLists(l1, l2)
display_linklist(result) # [1,1,2,3,4,4]

l1 = gen_linklist([])
l2 = gen_linklist([])
result = Solution().mergeTwoLists(l1, l2)
display_linklist(result) # []

l1 = gen_linklist([])
l2 = gen_linklist([0])
result = Solution().mergeTwoLists(l1, l2)
display_linklist(result) # [0]
