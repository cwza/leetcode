from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        "Simulation, Time: O(n), Space: O(1)"
        n = len(A)
        if n == 0 or n == 1 or n == 2: return 0

        start, end = 0, 0
        result = 0
        while end < n:
            # Go Up
            while end+1 < n and A[end+1] > A[end]:
                end += 1
            # Flat not Up
            if start == end:
                start += 1
                end = start
                continue
            peak = end
            # Go Down
            while end+1 < n and A[end+1] < A[end]:
                end += 1
            # Flat not Down
            if peak == end:
                start += 1
                end = start
                continue
            # Up then Down Case, Update result
            result = max(result, end-start+1)
            start = end
        return result

A = [2,1,4,7,3,2,5]
result = Solution().longestMountain(A)
assert result == 5

A = [2,2,2]
result = Solution().longestMountain(A)
assert result == 0