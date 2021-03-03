from typing import List

'''
This question is equal to find the longest 0's sequence length
Suppose it was K, then the solution should be (K+1)/2, if these 0's is not at 2 sides

For the 0's at 2 sides
The answer should be just the length of 0's

Take the max of these 3 values
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        "Time: O(n), Space: O(1)"
        i = 0 # pos of the first 1
        while seats[i] == 0:
            i += 1
        len_left_zeros = i # length of the most left 0's sequence

        j = len(seats) - 1 # pos of the last 1
        while seats[j] == 0:
            j -= 1
        len_right_zeros = len(seats) - 1 - j # length of the most right 0's sequence

        max_len_middle_zeros = 0
        K = 0 # len of zeros
        for x in range(i, j+1):
            if seats[x] == 0:
                K += 1
            else:
                max_len_middle_zeros = max(max_len_middle_zeros, (K+1)//2)
                K = 0
        return max(max_len_middle_zeros, len_left_zeros, len_right_zeros)

seats = [1,0,0,0,1,0,1]
result = Solution().maxDistToClosest(seats)
assert result == 2

seats = [1,0,0,0]
result = Solution().maxDistToClosest(seats)
assert result == 3

seats = [0,1]
result = Solution().maxDistToClosest(seats)
assert result == 1