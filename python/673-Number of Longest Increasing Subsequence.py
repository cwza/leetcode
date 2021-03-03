from typing import List

'''
length[i]: The LIS length from 0 to i, including i 
count[i]: The number of LIS from 0 to i, including i

Leetcode300 to get length[i]

Transition function:
count[i] =
1. for j = 0 ~ i-1:
       Find those j that make length[j] max
2. for such j in 1:
       if nums[i] > nums[j]:
           count[i] += length[j]
Initial:
count[i] = 1

result:
1. For i = 0 ~ n-1:
       Find those i that make length[i] max
2. for such i in 1:
       result += count[i]
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        "DP, Time: O(n^2), Space: O(n)"
        n = len(nums)
        if n == 0: return 0
        length = [1] * n
        count = [1] * n
        for i in range(1, n):
            max_len = -1
            max_count = (-1, -1) # len, count
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_len = max(max_len, length[j]+1)
                    if length[j] > max_count[0]:
                        max_count = (length[j], count[j])
                    elif length[j] == max_count[0]:
                        max_count = (max_count[0], count[j]+max_count[1])
            length[i] = max_len if max_len != -1 else 1
            count[i] = max_count[1] if max_count[0] != -1 else 1
        m = max(length)
        return sum([count[i] for i in range(n) if length[i] == m])

nums = [1,3,5,4,7]
result = Solution().findNumberOfLIS(nums)
assert result == 2

nums = [2,2,2,2,2]
result = Solution().findNumberOfLIS(nums)
assert result == 5