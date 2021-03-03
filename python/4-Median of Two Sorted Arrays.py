from typing import List

'''
For O(log(min(m, n)))
Use binary search and it is very tricky, see this video
https://www.youtube.com/watch?v=LPFhl65R7ww
'''

class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     "Merge, Time: O(m+n), Space: O(m+n)"
    #     if len(nums1) == 0 and len(nums2) == 0: return 0
    #     def merge(l1, l2):
    #         n = len(l1) + len(l2)
    #         l1.append(float("+inf"))
    #         l2.append(float("+inf"))
    #         result = []
    #         i, j = 0, 0
    #         for _ in range(n):
    #             if l1[i] <= l2[j]:
    #                 result.append(l1[i])
    #                 i += 1
    #             else:
    #                 result.append(l2[j])
    #                 j += 1
    #         return result
    #     merged = merge(nums1, nums2)
    #     n = len(merged)
    #     if n % 2 == 1:
    #         return merged[n//2]
    #     else:
    #         return ( merged[n//2] + merged[n//2-1] ) / 2
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     "Improvement of above, Time: O(m+n), Space: O(1)"
    #     if len(nums1) == 0 and len(nums2) == 0: return 0

    #     n = len(nums1) + len(nums2)
    #     end = n//2
    #     nums1.append(float("+inf"))
    #     nums2.append(float("+inf"))
    #     i, j = 0, 0
    #     results = []
    #     for k in range(end+1):
    #         if nums1[i] <= nums2[j]:
    #             if n % 2 == 1:
    #                 if k == end: results.append(nums1[i])
    #             else:
    #                 if k == end-1 or k == end: results.append(nums1[i])
    #             i += 1
    #         else:
    #             if n % 2 == 1:
    #                 if k == end: results.append(nums2[j])
    #             else:
    #                 if k == end-1 or k == end: results.append(nums2[j])
    #             j += 1
    #     return sum(results) / len(results)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        "Binary Search, Time: O(log(min(m, n))), Space: O(1)"
        # Make sure the nums1 is the small length one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        start, end = 0, x

        while start <= end:
            partition_x = (start+end) // 2
            partition_y = (x+y+1)//2 - partition_x
            x_left_max = float("-inf") if partition_x == 0 else nums1[partition_x-1]
            x_right_min = float("+inf") if partition_x == x else nums1[partition_x]
            y_left_max = float("-inf") if partition_y == 0 else nums2[partition_y-1]
            y_right_min = float("+inf") if partition_y == y else nums2[partition_y]

            if x_left_max <= y_right_min and y_left_max <= x_right_min:
                if (x+y)%2 == 0:
                    return (max(x_left_max, y_left_max) + min(x_right_min, y_right_min)) / 2
                else:
                    return max(x_left_max, y_left_max)
            elif x_left_max > y_right_min:
                end = partition_x - 1
            elif x_left_max <= y_right_min:
                start = partition_x + 1
        raise Exception("Opps")

nums1 = [1,3]
nums2 = [2]
result = Solution().findMedianSortedArrays(nums1, nums2)
assert result == 2

nums1 = [1,2]
nums2 = [3,4]
result = Solution().findMedianSortedArrays(nums1, nums2)
assert result == 2.5

nums1 = [0,0]
nums2 = [0,0]
result = Solution().findMedianSortedArrays(nums1, nums2)
assert result == 0

nums1 = []
nums2 = [1]
result = Solution().findMedianSortedArrays(nums1, nums2)
assert result == 1
