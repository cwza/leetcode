from linklist_helper import *
class Solution:
    def deleteDuplicates(self, head) -> ListNode:
        "Time: O(n), Space: O(1)"
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if prev != dummy and cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

head = gen_linklist([1, 1, 2])
result = Solution().deleteDuplicates(head)
display_linklist(result)

head = gen_linklist([1, 1, 2, 3, 3])
result = Solution().deleteDuplicates(head)
display_linklist(result)

head = gen_linklist([0])
result = Solution().deleteDuplicates(head)
display_linklist(result)
