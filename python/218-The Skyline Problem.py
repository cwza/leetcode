from typing import List
from functools import cmp_to_key
from sortedcontainers import SortedList

'''
Veryyyy Tricky and Veryyyy Hard
Alg explained:
https://www.youtube.com/watch?v=8Kd-Tn_Rz7s
Special case:
https://www.youtube.com/watch?v=GSBLe8cKu0s&t=647s

We need a data structure that can insert at O(logn), get_max at O(1), and remove element at O(logn)
That is balanced binary search tree.
For python, use SortedList from sortedcontainers
'''

class Event:
    def __init__(self, x: int, h: int, eventType: str):
        self.x = x
        self.h = h
        self.eventType = eventType # ENTER, LEAVE
    @classmethod
    def compare(cls, lhs: 'Event', rhs: 'Event'):
        '''
            first compare x, if they are same, use following logic
            If two ENTER events, then the one has higher height win
            If two LEAVE events, then the one has lower height win
            If one is ENTER and one is LEAVE, then the ENTER win
        '''
        if lhs.x != rhs.x:
            return lhs.x - rhs.x
        if lhs.eventType == 'ENTER' and rhs.eventType == 'ENTER':
            return rhs.h - lhs.h
        if lhs.eventType == 'LEAVE' and rhs.eventType == 'LEAVE':
            return lhs.h - rhs.h
        if lhs.eventType == 'ENTER' and rhs.eventType == 'LEAVE': 
            return -1
        return 1
    def __str__(self):
        return f'({self.x}, {self.h}, {self.eventType})'
    def __repr__(self):
        return str(self)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        "Sweep Line Alg with Balanced Binary Search Tree, Time: O(nlogn), Space: O(n)"
        # Generate events and sort them by special logic
        events = []
        for x1, x2, h in buildings:
            events.append(Event(x1, h, 'ENTER'))
            events.append(Event(x2, h, 'LEAVE'))
        events.sort(key=cmp_to_key(Event.compare)) # O(nlogn)

        # Run sweep line alg with bbst
        ds = SortedList([0])
        result = []
        for e in events:
            x, h, eventType = e.x, e.h, e.eventType
            if eventType == "ENTER":
                if h > ds[-1]: # O(1)
                    result.append([x, h])
                ds.add(h) # O(logn)
            else:
                ds.remove(h) # O(logn)
                if h > ds[-1]: # O(1)
                    result.append([x, ds[-1]])
        return result

buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] 
result = Solution().getSkyline(buildings)
assert result == [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]

buildings = [ [1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 7, 4], [8, 9, 4] ] 
result = Solution().getSkyline(buildings)
assert result == [ [1, 3], [2, 4], [4, 0], [5, 2], [6, 4], [7, 2], [8, 4], [9, 0] ]