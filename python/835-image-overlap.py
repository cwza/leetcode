from typing import List
from collections import Counter
'''
https://blog.csdn.net/fuxuemingzhu/article/details/82597238
'''
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        sz_A, sz_B = len(A), len(B)
        ones_A = [(i, j) for i in range(sz_A) for j in range(sz_A) if A[i][j] == 1]
        ones_B = [(i, j) for i in range(sz_B) for j in range(sz_B) if B[i][j] == 1]
        counter = Counter()
        for one_A in ones_A:
            for one_B in ones_B:
                diff = (one_B[0] - one_A[0], one_B[1] - one_A[1])
                counter[diff] += 1
        vals = counter.values()
        return max(vals) if len(vals) > 0 else 0

A = [[1,1,0],
     [0,1,0],
     [0,1,0]]
B = [[0,0,0],
     [0,1,1],
     [0,0,1]]
result = Solution().largestOverlap(A, B)
assert result == 3