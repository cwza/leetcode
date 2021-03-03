from typing import List

# class NumArray:
#     def __init__(self, nums: List[int]):
#         "Precompute, Time: O(n^2), Space: O(n^2), TLE"
#         n = len(nums)
#         dp = [[0]*n for _ in range(n)] # dp[i][j]: sum of [i, j]
#         for i in range(n):
#             for j in range(i, n):
#                 if i == j: 
#                     dp[i][j] = nums[i]
#                 else:
#                     dp[i][j] = dp[i][j-1] + nums[j]
#         self.dp = dp
#     def sumRange(self, i: int, j: int) -> int:
#         "Time: O(1)"
#         return self.dp[i][j]

class NumArray:
    def __init__(self, nums: List[int]):
        "Precompute, Time: O(n), Space: O(n)"
        n = len(nums)
        if n == 0:
            return
        dp = [0]*n # dp[i] = sum of [0, i]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i]
        self.dp = dp
    def sumRange(self, i: int, j: int) -> int:
        "Time: O(1)"
        "(i, j) = (0, j) - (0, i-1)"
        if self.dp is None: return 0
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]
        
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # return 1 ((-2) + 0 + 3)
print(numArray.sumRange(2, 5)) # return -1 (3 + (-5) + 2 + (-1)) 
print(numArray.sumRange(0, 5)) # return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

