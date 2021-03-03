from typing import List

'''
Approach 1:
Brute Force, Time: O(n^2), Space: O(1)
https://www.youtube.com/watch?v=HmBbcDiJapY

Approach 2:
Precomputed or DP, Time: O(n), Space: O(n)
https://www.youtube.com/watch?v=VZpJxINSvfs

Approach 3: This is tricky!!!
Min Max Trick with 2 Pointers, Time: O(n), Space: O(1)
https://www.youtube.com/watch?v=XqTBrQYYUcc
'''

class Solution:
    # def trap(self, height: List[int]) -> int:
    #     "Approach 1"
    #     n = len(height)
    #     if n < 3: return 0

    #     result = 0
    #     for i in range(n): # O(n)
    #         # left_max: max height from height[0, i]
    #         # right_max: max height from height[i, n-1]
    #         left_max = max(height[:i+1]) # O(n)
    #         right_max = max(height[i:])
    #         building_water_height = min(left_max, right_max)
    #         building_height = height[i]
    #         result += building_water_height - building_height
    #     return result
    # def trap(self, height: List[int]) -> int:
    #     "Approach 2"
    #     n = len(height)
    #     if n < 3: return 0

    #     # Pre-Compute left_max[0, n]
    #     left_max = [0]*n # left_max[i]: max height from height[0, i]
    #     left_max[0] = height[0]
    #     for i in range(1, n):
    #         left_max[i] = max(left_max[i-1], height[i])

    #     # Pre-Compute right_max[0, n]
    #     right_max = [0]*n # right_max[i]: max height from height[i, n-1]
    #     right_max[n-1] = height[n-1]
    #     for i in range(n-2, -1, -1):
    #         right_max[i] = max(right_max[i+1], height[i])
        
    #     # Accumulate the water height
    #     result = 0
    #     for i in range(n):
    #         result += min(left_max[i], right_max[i]) - height[i]

    #     return result
    def trap(self, height: List[int]) -> int:
        "Approach 3"
        '''
            We see a MinMax problem in our solution. 
            When we see a MinMax or MaxMin there is always an optimize solution that from 2 pointer or binary search.
            So think about them.
            The key point for this 2 pointer algorithm is that our left_max[i] is monotonic increasing and our right_max[i] is monotonic decreasing.
            This algorithm is tricky. Please see https://www.youtube.com/watch?v=XqTBrQYYUcc
        '''
        n = len(height)
        if n < 3: return 0

        left_max, right_max = 0, 0
        result = 0
        i, j = 0, n - 1

        while i <= j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max <= right_max:
                result += left_max - height[i]
                i += 1
            else:
                result += right_max - height[j]
                j -= 1
        
        return result



height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = Solution().trap(height)
assert result == 6

height = [4,2,0,3,2,5]
result = Solution().trap(height)
assert result == 9