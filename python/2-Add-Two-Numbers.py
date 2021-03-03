from linklist_helper import *

'''
You can't just generate 2 integers from list and add them up.
This problem is assumed that these 2 numbers are too large that it can't be load in to 32 bit integers.
Just iterate through these 2 list and add digits one by one.
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        "Time: O(max(m, n)), Space: O(max(m, n))"
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + carry
            carry, remain = divmod(val, 10)
            cur.next = ListNode(remain)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next

l1 = gen_linklist([2, 4, 3])
l2 = gen_linklist([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
display_linklist(result) # 708

l1 = gen_linklist([1, 8])
l2 = gen_linklist([0])
result = Solution().addTwoNumbers(l1, l2)
display_linklist(result) # 18