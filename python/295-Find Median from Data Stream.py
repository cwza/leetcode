from sortedcontainers import SortedList

def get_median_from_sorted(sorted_nums):
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[(n-1)//2] + sorted_nums[(n-1)//2+1]) / 2
    else:
        median = sorted_nums[(n-1)//2]
    return median
# class MedianFinder:
#     "Sort"
#     def __init__(self):
#         "Space: O(n)"
#         self.nums = []
#     def addNum(self, num: int) -> None:
#         "Time: O(nlogn)"
#         self.nums.append(num)
#         self.nums.sort()
#     def findMedian(self) -> float:
#         "Time: O(1)"
#         return get_median_from_sorted(self.nums)
# class MedianFinder:
#     "Insertion"
#     def __init__(self):
#         "Space: O(n)"
#         self.nums = []
#     def addNum(self, num: int) -> None:
#         "Time: O(n)"
#         self.nums.append(float("+inf"))
#         n = len(self.nums)
#         for i in range(n):
#             if self.nums[i] >= num:
#                 self.nums.insert(i, num)
#                 break
#         del self.nums[-1]
#     def findMedian(self) -> float:
#         "Time: O(1)"
#         return get_median_from_sorted(self.nums)
class MedianFinder:
    "SortedList or Balanced Binary Search Tree"
    def __init__(self):
        "Space: O(n)"
        self.nums = SortedList()
    def addNum(self, num: int) -> None:
        "Time: O(logn)"
        self.nums.add(num)
    def findMedian(self) -> float:
        "Time: O(1)"
        return get_median_from_sorted(self.nums)

median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)
print(median_finder.findMedian()) # 1.5
median_finder.addNum(3) 
print(median_finder.findMedian()) # 2

median_finder = MedianFinder()
median_finder.addNum(-1)
median_finder.addNum(-2)
print(median_finder.findMedian()) # -1.5