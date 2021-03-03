from collections import defaultdict
from math import ceil

class TimeMap:
    "Binary Search"
    def __init__(self):
        "Space: O(n)"
        self.table = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        "Time: O(1)"
        self.table[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        "Time: O(logc)"
        values = self.table[key]

        l, r = 0, len(values)
        while l < r:
            m = l + (r-l)//2
            if values[m][1] > timestamp: r = m
            else: l = m + 1
        if l-1 < 0 : return ""
        return values[l-1][0]

kv = TimeMap()   
kv.set("foo", "bar", 1) # store the key "foo" and value "bar" along with timestamp = 1   
print(kv.get("foo", 1))  # output "bar"   
print(kv.get("foo", 3)) # output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4)   
print(kv.get("foo", 4)) # output "bar2"   
print(kv.get("foo", 5)) #output "bar2"   
        
