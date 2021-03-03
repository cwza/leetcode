from linklist_helper import *

'''
Solve this with Space: O(1)
Suppose inputs a = [1, 0, 1, 1]
b[i] is the answer that from a[0] ~ a[i]
ex: 
b[0] = 2^0 * a[0] = 1(1), 
b[1] = 2^1 * a[0] + 2^0 * a[1] = 2(10)
b[2] = 2^2 * a[0] + 2^1 * a[1] + 2^0 * a[2] = 5(101)
b[3] = 2^3 * a[0] + 2^2 * a[1] + 2^1 * a[2] + 2^0 * a[3] = 11(1011)
=> b[i] = 2 * b[i-1] + a[i]
=> b[0] = a[0]
=> answer: b[n-1]

Space: O(n)
b[0] = a[0]
for i = 1 ~ n-1:
    b[i] = 2 * b[i-1] + a[i]
return b[n-1]

Space: O(1)
b = a[0]
for i = 1 ~ n-1:
    b = 2 * b + a[i]
return b
'''

class Solution:
    # def getDecimalValue(self, head: ListNode) -> int:
    #     "Time: O(n), Space: O(n)"
    #     strs = ""
    #     while head is not None:
    #         strs += str(head.val)
    #         head = head.next
    #     return int(strs, 2)
    # def getDecimalValue(self, head: ListNode) -> int:
    #     "Time: O(n), Space: O(1)"
    #     b = head.val
    #     while head.next is not None:
    #         b = 2 * b + head.next.val
    #         head = head.next
    #     return b
    def getDecimalValue(self, head: ListNode) -> int:
        "Bit Operation of above because val is 0 or 1, Time: O(n), Space: O(1)"
        b = head.val
        while head.next is not None:
            b = b << 1 | head.next.val
            head = head.next
        return b

head = gen_linklist([1,0,1])
result = Solution().getDecimalValue(head)
assert result == 5

head = gen_linklist([0])
result = Solution().getDecimalValue(head)
assert result == 0

head = gen_linklist([1])
result = Solution().getDecimalValue(head)
assert result == 1

head = gen_linklist([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
result = Solution().getDecimalValue(head)
assert result == 18880

head = gen_linklist([0,0])
result = Solution().getDecimalValue(head)
assert result == 0