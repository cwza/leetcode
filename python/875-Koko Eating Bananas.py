from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        "Binary Search, Time: O(nlogm), Space: O(1), n=len(piles), m = max(piles)"
        def g(m):
            h = 0
            for pile in piles:
                h += ceil(pile/m)
                if h > H: return False
            return True
        l, r = 1, max(piles)+1
        while l < r:
            m = l + (r-l)//2
            if g(m): r = m
            else: l = m + 1
        if l == max(piles)+1: raise Exception("Suck")
        return l

piles = [3,6,7,11]
H = 8
result = Solution().minEatingSpeed(piles, H)
assert result == 4

piles = [30,11,23,4,20]
H = 5
result = Solution().minEatingSpeed(piles, H)
assert result == 30

piles = [30,11,23,4,20]
H = 6
result = Solution().minEatingSpeed(piles, H)
assert result == 23