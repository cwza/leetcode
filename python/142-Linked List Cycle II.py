from linklist_helper import *

'''
Floyd's Algorithm
起點設2個指標，分別為Slow與Fast。
每次的循環，Slow往前1步、Fast往前2步
當Fast走到結尾點null，代表此Linked List無環；否則當Slow和Fast的位置相同時，代表此Linked List有環。
把相同位置的Node用另一個ListNode變數meetNode記住，使Slow回到起點(Head)
Slow和meetNode以同樣速度往前移動，當他們走到相同位置時，則那位置是環的進入點。
Proof:
https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
'''

class Solution:
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     "set, Time: O(n), Space: O(n)"
    #     if head is None or head.next is None: return None
    #     check_dup = set()
    #     while head:
    #         if head in check_dup:
    #             return head
    #         else:
    #             check_dup.add(head)
    #             head = head.next
    #     return None
    def detectCycle(self, head: ListNode) -> ListNode:
        "Floyd's Alg, Time: O(n), Space: O(1)"
        if head is None or head.next is None: return None
        slow, fast = head, head

        while True:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        slow = head
        while True:
            if slow == fast:
                return slow
            else:
                slow = slow.next
                fast = fast.next
