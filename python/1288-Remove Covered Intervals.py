from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        "O(nlogn)"
        if len(intervals) == 1: return 1

        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        n = len(intervals)
        overlap = 0
        prev_interval = intervals[0]
        for cur_interval in intervals[1:]:
            if prev_interval[0] <= cur_interval[0] and prev_interval[1] >= cur_interval[1]: # prev covers cur
                overlap += 1
            elif cur_interval[0] <= prev_interval[0] and cur_interval[1] >= prev_interval[1]: # cur cover prev
                overlap += 1
                prev_interval = cur_interval
            else:
                prev_interval = cur_interval
        return n - overlap

intervals = [[1,4],[3,6],[2,8]]
result = Solution().removeCoveredIntervals(intervals)
assert result == 2

intervals = [[1,4],[2,3]]
result = Solution().removeCoveredIntervals(intervals)
assert result == 1

intervals = [[0,10],[5,12]]
result = Solution().removeCoveredIntervals(intervals)
assert result == 2

intervals = [[3,10],[4,10],[5,11]]
result = Solution().removeCoveredIntervals(intervals)
assert result == 2

intervals = [[1,2],[1,4],[3,4]]
result = Solution().removeCoveredIntervals(intervals)
assert result == 1
