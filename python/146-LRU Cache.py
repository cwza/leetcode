from __future__ import annotations
from typing import Optional, Dict, OrderedDict
from dataclasses import dataclass

'''
https://www.youtube.com/watch?v=iuqZvajTOyA
'''

@dataclass
class Node:
    key: int
    val: int
    prev: Optional[Node] = None
    nxt: Optional[Node] = None
class DoublyList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
    def remove(self, node: Optional[Node]):
        "O(1)"
        if node is None: return
        if node != self.head and node != self.tail:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
        else:
            if node == self.head:
                self.head = node.nxt
                if self.head is not None: self.head.prev = None
            if node == self.tail:
                self.tail = node.prev
                if self.tail is not None: self.tail.nxt = None
    def push_left(self, node: Node):
        "O(1)"
        if self.head is not None:
            node.nxt = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
        else:
            node.prev = None
            node.nxt = None
            self.head = node
            self.tail = node
    def __str__(self):
        cur = self.head
        result = ""
        while cur is not None:
            result += f" {str(cur)}"
            cur = cur.nxt
        return result
# class LRUCache:
#     "Hash Map + Doubly linked list"
#     def __init__(self, capacity: int):
#         self.capacity: int = capacity
#         self.map: Dict[int, Node] = {}
#         self.dlist = DoublyList()
#     def get(self, key: int) -> int:
#         "O(1)"
#         if key not in self.map:
#             return -1
#         node = self.map[key]
#         self.dlist.remove(node)
#         self.dlist.push_left(node)
#         return node.val
#     def put(self, key: int, value: int) -> None:
#         "O(1)"
#         if key in self.map:
#             node = self.map[key]
#             node.val = value
#             self.dlist.remove(node)
#             self.dlist.push_left(node)
#         else:
#             if len(self.map) >= self.capacity:
#                 old = self.dlist.tail
#                 self.dlist.remove(old)
#                 del self.map[old.key]
#             node = Node(key, value)
#             self.map[key] = node
#             self.dlist.push_left(node)

class LRUCache:
    "Use python3 OrderedDict"
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.map: OrderedDict[int, int] = OrderedDict()
    def get(self, key: int) -> int:
        "OrderedDict.move_to_end: O(1)"
        if key not in self.map:
            return -1
        self.map.move_to_end(key, last=False)
        return self.map[key]
    def put(self, key: int, value: int) -> None:
        "OrderedDict.popitem: O(1)"
        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key, last=False)
        else:
            if len(self.map) >= self.capacity:
                self.map.popitem(last=True)
            self.map[key] = value
            self.map.move_to_end(key, last=False)

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))   # return -1 (not found)
print(lRUCache.get(3))   # return 3
print(lRUCache.get(4))    # return 4

print()

lRUCache = LRUCache(2)
lRUCache.put(2, 1); # cache is {2=1}
lRUCache.put(2, 2); # cache is {2=2}
print(lRUCache.get(2))    # return 2
lRUCache.put(1, 1) # cache is {2=2, 1=1}
lRUCache.put(4, 1) # LRU key was 4, evicts key 2, cache is {1=1, 4=1}
print(lRUCache.get(2))    # returns -1 (not found)