from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        "Greedy, Time: O(3n), Space: can be O(1)"
        # Find the value that appears in all (a, b)s
        nums = set([A[0], B[0]])
        for a, b in zip(A, B):
            nums.intersection_update(set([a, b]))
            if len(nums) == 0: return -1
        # Compare the 2 swap
        if len(nums) == 1 or len(nums) == 2:
            num = nums.pop()
            return min(sum([1 for a in A if a != num]), sum(1 for b in B if b != num))
        raise Exception("Impossible")

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
result = Solution().minDominoRotations(A, B)
assert result == 2

A = [3,5,1,2,3]
B = [3,6,3,3,4]
result = Solution().minDominoRotations(A, B)
assert result == -1