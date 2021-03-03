from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        "Simulation, Time: O(n), Space: O(1)"
        n = len(arr)
        if n < 3: return False
        i = 0
        while i < n-1 and arr[i] < arr[i+1]:
            i += 1
        peak = i
        if peak == 0 or peak == n-1:
            return False 
        for i in range(peak, n-1):
            if arr[i] <= arr[i+1]:
                return False
        return True

arr = [2,1]
result = Solution().validMountainArray(arr)
assert result == False

arr = [3,5,5]
result = Solution().validMountainArray(arr)
assert result == False

arr = [0,3,2,1]
result = Solution().validMountainArray(arr)
assert result == True