
__all__ = ['ListNode', 'gen_linklist', 'display_linklist']

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f'{self.val}'

def gen_linklist(vals):
    if len(vals) == 0: return None
    head = ListNode(vals[0])
    prev = head
    for i in range(1, len(vals)):
        node = ListNode(vals[i])
        prev.next = node
        prev = node
    return head
def display_linklist(head):
    result = []
    pres = head
    while pres is not None:
        result.append(pres.val)
        pres = pres.next
    print(result)


if __name__ == "__main__":
    l = [1,2,3,4]
    l = []
    l = [4, 5]
    display_linklist(gen_linklist(l))