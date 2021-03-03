from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        "Binary Search on col[0] then binary search on row, Time: O(logm) + O(logn)"
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        # Find the largest one in col_0 that <= target
        l, r = 0, m
        while l < r:
            m = l + (r-l)//2
            if matrix[m][0] > target: r = m
            else: l = m + 1
        row_idx = l-1
        if row_idx == -1: return False
        # Find the target at matrix[row_idx]
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            if matrix[row_idx][m] == target: return True
            elif matrix[row_idx][m] > target: r = m
            else: l = m + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
result = Solution().searchMatrix(matrix, target)
assert result == True

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 13
result = Solution().searchMatrix(matrix, target)
assert result == False

matrix = []
target = 0
result = Solution().searchMatrix(matrix, target)
assert result == False