from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        "Time: O(nlogn), Space: O(1)"
        n = len(intervals)
        if n == 0: return 0

        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        result = 0
        for i in range(1, n):
            cur = intervals[i]
            if prev[1] <= cur[0]:
                prev = cur
            else:
                result += 1
                if cur[1] < prev[1]:
                    prev = cur
        return result

intervals = [[1,2],[2,3],[3,4],[1,3]]
result = Solution().eraseOverlapIntervals(intervals)
assert result == 1

intervals = [[1,2],[1,2],[1,2]]
result = Solution().eraseOverlapIntervals(intervals)
assert result == 2

intervals = [[1,2],[2,3]]
result = Solution().eraseOverlapIntervals(intervals)
assert result == 0

intervals = [[1,100],[11,22],[1,11],[2,12]]
result = Solution().eraseOverlapIntervals(intervals)
assert result == 2