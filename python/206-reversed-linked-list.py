from linklist_helper import ListNode, gen_linklist, display_linklist

'''
recursive:
init:
    head: 1 -> 2 -> 3 -> 4 -> 5 -> None

1. new_head = reverseList(head.next): 5 -> 4 -> 3 -> 2 -> None
   head becomes 1 -> 2 -> None
2. head.next.next = head
   new_head: 5 -> 4 -> 3 -> 2 -> 1 -> 2 ...
   head: 1 -> 2 -> 1 .....
3. head.next = None
   new_head: 5 -> 4 -> 3 -> 2 -> 1 -> None

Non-recursive:
Init:
    1 -> 2 -> 3 -> 4 -> 5 -> N
    prev = None
    cur = 1
After 1st iter:
    1 -> N, 2 -> 3 -> 4 -> 5 -> N
    prev = 1
    cur = 2
After 2nd iter:
    2 -> 1 -> N, 3 -> 4 -> 5 -> N
    prev = 2
    cur = 3
After 3rd iter:
    3 -> 2 -> 1 -> N, 4 -> 5 -> N
    prev = 3
    cur = 4
After 4th iter:
    4 -> 3 -> 2 -> 1 -> N, 5 -> N
    prev = 4
    cur = 5
After 5th iter:
    5 -> 4 -> 3 -> 2 -> 1 -> N
    prev = 5
    cur = N
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        "Recursive, Time: O(n), Space: O(n) for recursive stack"
        if head is None or head.next is None: return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
    def reverseList(self, head: ListNode) -> ListNode:
        "Iterative, Time: O(n), Space: O(1)"
        if head is None: return head
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

l = [1, 2, 3, 4, 5]
head = gen_linklist(l)
result = Solution().reverseList(head)
display_linklist(result)