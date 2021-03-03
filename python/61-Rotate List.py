from linklist_helper import *

'''
Suppose we have head, new_head_prev(node that just before new head), new_head, tail 
tail.next = head
new_head_prev.next = None
return new_head

How to find new_head_prev and tail??
1. One pass to get list length n and tail node
2. The new_head_prev is at n - k%n - 1, Another one pass to get there

Note that if k%n==0, n-k%n-1==n-1, then new_head_prev be n-1, 
if you use new_head = new_head_prev.next this new_head will be set to None, but it should be at 0
so when k%n==0, directly return head
'''

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        "2 Pass, Time: O(n), Space: O(1)"
        if head is None or head.next is None: return head
        # One pass to get n and tail
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        if k%n == 0: return head
        # One pass to get new_head_prev and new_head
        new_head_prev = head
        for _ in range(n-k%n-1):
            new_head_prev = new_head_prev.next
        new_head = new_head_prev.next
        # relink new_head_prev, new_head, tail, head to get result
        tail.next = head
        new_head_prev.next = None
        return new_head

head = gen_linklist([1, 2, 3, 4, 5])
k = 2
result = Solution().rotateRight(head, k)
display_linklist(result) # [4, 5, 1, 2, 3]

head = gen_linklist([0, 1, 2])
k = 4
result = Solution().rotateRight(head, k)
display_linklist(result) # [2, 0, 1]

head = gen_linklist([1, 2])
k = 0
result = Solution().rotateRight(head, k)
display_linklist(result) # [1, 2]