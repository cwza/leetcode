from typing import List

'''
https://blog.techbridge.cc/2020/01/16/leetcode-刷題-pattern-merge-intervals/

First we sort the intervals by start, then the conditions of each 2 intervals reduced to following 3 patterns.

1.
a: -----
b:    -----
a.end >= b.start so need to merge
==> merged: (a.start, max(a.end, b.end))

2. 
a: -----
b:  ---
a.end >= b.start so need to merge
==> merged: (a.start, max(a.end, b.end))

3. 
a: -----
b:        ---
a.end < b.start so do not need to merge
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        "O(nlogn)"
        if len(intervals) == 0: return []

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            a = result[-1]
            b = intervals[i]
            if a[1] >= b[0]:
                merged = [a[0], max(a[1], b[1])]
                result[-1] = merged
            else:
                result.append(b)

        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
result = Solution().merge(intervals)
assert result == [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
result = Solution().merge(intervals)
assert result == [[1,5]]