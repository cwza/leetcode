from linklist_helper import ListNode, gen_linklist, display_linklist

'''
Two pointer slow, fast
When fast go to last, the slow is the middle point
https://www.youtube.com/watch?v=wmpivqMlClI
'''
class Solution:
    '''
        [1,2,3,4,5] -> 3
        [1,2,3,4,5,6] -> 4
    '''
    def middleNode(self, head: ListNode) -> ListNode:
        "Time: O(n), Space: O(1)"
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

l = [1,2,3,4,5]
l = [1,2,3,4,5,6]
head = gen_linklist(l)
result = Solution().middleNode(head)
print(result)