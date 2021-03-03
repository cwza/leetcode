from linklist_helper import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        "Recursive, Time: O(n), Space: O(n)"
        if head is None or head.next is None: return head
        new_head = head.next
        nxt = new_head.next
        new_head.next = head
        head.next = self.swapPairs(nxt)
        return new_head

head = gen_linklist([1,2,3,4])
result = Solution().swapPairs(head)
display_linklist(result) # [2,1,4,3]

head = gen_linklist([])
result = Solution().swapPairs(head)
display_linklist(result) # []

head = gen_linklist([1])
result = Solution().swapPairs(head)
display_linklist(result) # [1]