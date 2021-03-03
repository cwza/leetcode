from typing import List
from collections import Counter

'''
Square:
1. Four edges have the same length
2. 2 diagonals have the same length but different from four edges
'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        "Time: O(1), Space: O(1)"
        def get_length(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        points = [p1, p2, p3, p4]
        lens = Counter()
        for i in range(3):
            for j in range(i+1, 4):
                length = get_length(points[i], points[j])
                lens[length] += 1
        lens = list(lens.values())
        return lens == [2, 4] or lens == [4, 2]

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
result = Solution().validSquare(p1, p2, p3, p4)
assert result == True