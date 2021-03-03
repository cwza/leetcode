from typing import List
from collections import Counter

class Solution:
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     "One Hash, O(n^3) TLE"
    #     counter = Counter(D)
    #     result = 0
    #     for i, num1 in enumerate(A):
    #         for j, num2 in enumerate(B):
    #             for k, num3 in enumerate(C):
    #                 complement = 0 - num1 - num2 - num3
    #                 if complement in counter:
    #                     result += counter[complement]
    #     return result
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        "2 Hash Table, O(n^2)"
        n = len(A)
        counterAB = Counter()
        counterCD = Counter()
        for i in range(n):
            for j in range(n):
                counterAB[A[i]+B[j]] += 1
                counterCD[C[i]+D[j]] += 1
        result = 0
        for a in counterAB.keys():
            if -a in counterCD:
                result += counterAB[a] * counterCD[-a]
        return result

# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# result = Solution().fourSumCount(A, B, C, D)
# assert result == 2

A = [1]
B = [-1]
C = [0]
D = [1]
result = Solution().fourSumCount(A, B, C, D)
assert result == 0