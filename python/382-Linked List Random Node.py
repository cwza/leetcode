from linklist_helper import *
import random

'''
Reservoir sampling
https://en.wikipedia.org/wiki/Reservoir_sampling
'''

class Solution:
    def __init__(self, head: ListNode):
        "Naive array, Time: O(n), Space: O(n)"
        self.vals = []
        while head is not None:
            self.vals.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        "Time: O(1)"
        return random.choice(self.vals)

# class Solution:
#     def __init__(self, head: ListNode):
#         self.head = head
#     def getRandom(self) -> int:
#         "Reservoir Sampling, Time: O(n), Space: O(1)"
#         result = -1
#         node = self.head
#         i = 1
#         # replace elements with gradually decreasing probability
#         while node:
#             j = random.randint(1, i)
#             if j <= 1:
#                 result = node.val
#             node = node.next
#             i += 1
#         return result
        
        

from collections import Counter
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
solution = Solution(head)
print(Counter([solution.getRandom() for _ in range(3000)]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()