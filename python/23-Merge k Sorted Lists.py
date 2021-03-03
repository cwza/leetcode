from typing import List
from linklist_helper import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        "Approach2, Time: O(NK), Space: O(1), N: total number of nodes, K: len(lists), TLE"
        def find_min(lists):
            idx = -1
            res = ListNode(float("+inf"))
            for i, l in enumerate(lists):
                if l is None: continue
                if l.val < res.val: 
                    idx = i
                    res = l
            return idx, res
        dummy = ListNode()
        cur = dummy
        while True:
            idx, min_node = find_min(lists)
            if idx == -1: break
            cur.next = min_node
            cur = cur.next
            lists[idx] = lists[idx].next
        return dummy.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        "Approach3 use heap to improve above, Time: O(NlogK), Space: O(1)"
        import heapq
        min_heap = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(min_heap)

        dummy = ListNode()
        cur = dummy
        while min_heap:
            _, idx = heapq.heappop(min_heap)
            min_node = lists[idx]
            cur.next = min_node
            cur = cur.next
            lists[idx] = lists[idx].next
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.val, idx))
        return dummy.next

lists = [gen_linklist([1,4,5]),gen_linklist([1,3,4]),gen_linklist([2,6])]
ans = Solution().mergeKLists(lists)
display_linklist(ans)