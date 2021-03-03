from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        "Time: O(m+n), Space: O(m+n) for return"
        l, r = 0, 0
        result = []
        while l < len(A) and r < len(B):
            if A[l][0] <= B[r][0]: a, b = A[l], B[r]
            else: a, b = B[r], A[l]
            if A[l][1] <= B[r][1]: l += 1
            else: r += 1
            if a[1] < b[0]: continue
            else: result.append([b[0], min(a[1], b[1])])
        return result

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
result = Solution().intervalIntersection(A, B)
assert result == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]