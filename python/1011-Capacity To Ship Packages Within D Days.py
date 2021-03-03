from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        "Binary Search, Time: O(nlogn), Space: O(1)"
        def g(m):
            d = 1
            total = 0
            for weight in weights:
                total += weight
                if total > m:
                    d += 1
                    total = weight
                    if d > D:
                        return False
            return True
        l, r = max(weights), sum(weights)+1
        while l < r:
            m = l + (r-l)//2
            if g(m): r = m
            else: l = m + 1
        if l == sum(weights)+1: raise Exception("Suck")
        return l

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
result = Solution().shipWithinDays(weights, D)
assert result == 15

weights = [3,2,2,4,1,4]
D = 3
result = Solution().shipWithinDays(weights, D)
assert result == 6

weights = [1,2,3,1,1]
D = 4
result = Solution().shipWithinDays(weights, D)
assert result == 3