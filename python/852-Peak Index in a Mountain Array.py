from typing import List

class Solution:
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     "Linear Search, Time: O(n), Space: O(1)"
    #     for i in range(len(arr)-1):
    #         if arr[i+1] < arr[i]:
    #             return i
    #     return -1
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        "Binary Search, Time: O(logn), Space: O(1)"
        "Look at Linear Search, it's like we want to find the minimal i that satisfies arr[i+1] < arr[i]"
        "So we can use binary search template to solve this problem"
        l, r = 0, len(arr)
        while l < r:
            m = l + (r-l)//2
            if arr[m+1] < arr[m]: r = m
            else: l = m + 1
        if l == len(arr): return -1
        return l

arr = [0,1,0]
result = Solution().peakIndexInMountainArray(arr)
assert result == 1

arr = [0,2,1,0]
result = Solution().peakIndexInMountainArray(arr)
assert result == 1

arr = [0,10,5,2]
result = Solution().peakIndexInMountainArray(arr)
assert result == 1

arr = [3,4,5,1]
result = Solution().peakIndexInMountainArray(arr)
assert result == 2

arr = [24,69,100,99,79,78,67,36,26,19]
result = Solution().peakIndexInMountainArray(arr)
assert result == 2