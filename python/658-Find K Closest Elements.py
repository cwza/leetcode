from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        "Sliding Window, Time: O(n), Space: O(k) for returns"
        n = len(arr)
        best_i = 0
        dist = sum([abs(arr[i]-x) for i in range(k)])
        for i in range(1, n-k+1):
            new_dist = dist - abs(arr[i-1]-x) + abs(arr[i+(k-1)]-x)
            if new_dist < dist:
                dist = new_dist
                best_i = i
        return arr[best_i:best_i+k]
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        "Binary Search, Time: O(logn+k), Space: O(k) for returns"
        # Binary search to find the minimal that larger than or equal to target
        n = len(arr)
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            if arr[m] >= x: r = m
            else: l = m + 1
        # Two pointer to find the result
        l, r = l-1, l
        while k:
            k -= 1
            if r == n: l -= 1
            elif l < 0: r += 1
            elif abs(arr[l]-x) <= abs(arr[r]-x): l -= 1
            else: r += 1
        return arr[l+1:r]

arr = [1,2,3,4,5]
k = 4
x = 3
result = Solution().findClosestElements(arr, k, x)
assert result == [1,2,3,4]

arr = [1,2,3,4,5]
k = 4
x = -1
result = Solution().findClosestElements(arr, k, x)
assert result == [1,2,3,4]

arr = [1,1,1,10,10,10]
k = 1
x = 9
result = Solution().findClosestElements(arr, k, x)
assert result == [10]

arr = [0,1,2,2,2,3,6,8,8,9]
k = 5
x = 9
result = Solution().findClosestElements(arr, k, x)
# assert result == [10]