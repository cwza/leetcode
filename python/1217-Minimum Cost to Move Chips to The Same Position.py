from typing import List

'''
Easy but tricky solution using greedy.

Key: 
We can move all chips at even positions to position 2, and move all chips at the odd positions to position 1 with cost 0.
After that all chips are at position 1 and 2.
Then the smallest cost to move all chips to the same position is the smaller number of chips at postion 1 and 2.

Algorithm:
1. Count even number, Count odd number
2. return the smaller one
'''

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        "Greedy, Time: O(n), Space: O(1)"
        num_even = 0
        num_odd = 0
        for num in position:
            if num % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
        return min(num_even, num_odd)

position = [1,2,3]
result = Solution().minCostToMoveChips(position)
assert result == 1

position = [2,2,2,3,3]
result = Solution().minCostToMoveChips(position)
assert result == 2

position = [1,1000000000]
result = Solution().minCostToMoveChips(position)
assert result == 1