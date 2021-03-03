from linklist_helper import *

class Solution:
    # def isPalindrome(self, head) -> bool:
    #     "Time: O(n), Space: O(n)"
    #     arr = []
    #     while head:
    #         arr.append(head.val)
    #         head = head.next
    #     return arr == arr[::-1]
    def isPalindrome(self, head) -> bool:
        "Time: O(n), Space: O(1)"
        if head is None or head.next is None: return True
        def find_mid(head):
            slow, fast = head, head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            if fast is not None: # odd number of nodes, we need the next
                slow = slow.next
            return slow
        def reverse(head):
            cur = head
            prev = None
            while True:
                nxt = cur.next
                cur.next = prev
                if nxt is None:
                    return cur
                prev = cur
                cur = nxt

        mid = find_mid(head)
        right = reverse(mid)
        left = head
        while right is not None:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True

head = gen_linklist([1, 2])
result = Solution().isPalindrome(head)
assert result == False

head = gen_linklist([1, 2, 2, 1])
result = Solution().isPalindrome(head)
assert result == True

head = gen_linklist([1])
result = Solution().isPalindrome(head)
assert result == True