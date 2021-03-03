from typing import List

'''
In each row, the ith value from the left is equal to the inverse of the ith value from the right.
'''

class Solution:
    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    #     "Time: O(2n^2), Space: O(1)"
    #     for row in A:
    #         row.reverse()
    #     for row in A:
    #         n = len(row)
    #         for j in range(n):
    #             row[j] ^= 1
    #     return A
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        "Time: O(n^2), Space: O(1)"
        for row in A:
            n = len(row)
            for j in range((n+1)//2):
                # row[j], row[n-1-j] = row[n-1-j] ^ 1, row[j] ^ 1
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1
        return A

A = [[1,1,0],
     [1,0,1],
     [0,0,0]]
result = Solution().flipAndInvertImage(A)
assert result == [[1,0,0],
                  [0,1,0],
                  [1,1,1]]

A = [[1,1,0,0],
     [1,0,0,1],
     [0,1,1,1],
     [1,0,1,0]]
result = Solution().flipAndInvertImage(A)
assert result == [[1,1,0,0],
                  [0,1,1,0],
                  [0,0,0,1],
                  [1,0,1,0]]
