from linklist_helper import *
from collections import deque

'''
You can't just generate 2 integers from list and add them up.
This problem is assumed that these 2 numbers are too large that it can't be load in to 32 bit integers.
Just iterate through these 2 list and add digits one by one.

Solution1:
1. reverse 2 list (LeetCode 206)
2. add two list (LeetCode 2)
3. reverse result list from 2 (LeetCode 206)

Solution2:
Use stack
1. push 2 list value into 2 stack
2. pop the value from 2 stack and add each digit and generate ListNode from right to left
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        "Solution2, Time: O(n+m), Space: O(n+m)"
        def list_to_stack(head):
            stack = deque()
            while head is not None:
                stack.append(head.val)
                head = head.next
            return stack
        stack1 = list_to_stack(l1)
        stack2 = list_to_stack(l2)

        carry = 0
        node = None
        while not (len(stack1) == 0 and len(stack2) == 0) :
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            s = a + b + carry
            val = s % 10
            carry = s // 10
            new_node = ListNode(val)
            new_node.next = node
            node = new_node
        if carry != 0:
            new_node = ListNode(carry)
            new_node.next = node
            node = new_node
        return node

l1 = gen_linklist([7, 2, 4, 3])
l2 = gen_linklist([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2) # [7, 8, 0, 7]
display_linklist(result)