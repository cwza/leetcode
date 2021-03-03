from linklist_helper import *

'''
https://www.youtube.com/watch?v=N1VVLLan6S0
'''

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        "Time: O(n^2), Space: O(1)"
        if head is None or head.next is None: return head
        dummy = ListNode(float("-inf"))
        dummy.next = head
        j_prev = head

        while j_prev.next is not None:
            j = j_prev.next
            if j.val >= j_prev.val:
                j_prev = j_prev.next
                continue

            i = dummy
            j_prev.next = j.next
            while i.next.val < j.val:
                i = i.next
            j.next = i.next
            i.next = j
        return dummy.next

head = gen_linklist([4, 2, 1, 3])
result = Solution().insertionSortList(head)
display_linklist(result)

head = gen_linklist([-1, 5, 3, 4, 0])
result = Solution().insertionSortList(head)
display_linklist(result)