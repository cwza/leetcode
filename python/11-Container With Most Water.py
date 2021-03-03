from typing import List

'''
One pass is tricky please see:

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.
We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 
Futher, we maintain a variable maxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.
https://www.youtube.com/watch?v=cPwXGcZQ1mA&ab_channel=JoyLiu-ComputerPsyc
'''

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(1), TLE"
    #     n = len(height)
    #     max_area = 0
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             left = height[i]
    #             right = height[j]
    #             area = (j - i) * min(left, right)
    #             max_area = max(max_area, area)
    #     return max_area
    def maxArea(self, height: List[int]) -> int:
        "Two pointer one pass, Time: O(n/2), Space: O(1)"
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            left = height[i]
            right = height[j]
            area = (j - i) * min(left, right)
            max_area = max(max_area, area)
            if left <= right:
                i += 1
            else:
                j -= 1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(height)
assert result == 49

height = [1,1]
result = Solution().maxArea(height)
assert result == 1

height = [4,3,2,1,4]
result = Solution().maxArea(height)
assert result == 16

height = [1,2,1]
result = Solution().maxArea(height)
assert result == 2