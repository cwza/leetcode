from typing import List

'''
Very Like Merge Intervals
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        "Time: O(nlogn), Space: O(1)"
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])
        a = points[0]
        result = 1
        for i in range(1, len(points)):
            b = points[i]
            if b[0] > a[1]:
                result += 1
                a = b
            else:
                a = [b[0], min(a[1], b[1])]
        return result

points = [[10,16],[2,8],[1,6],[7,12]]
result = Solution().findMinArrowShots(points)
assert result == 2

points = [[1,2],[3,4],[5,6],[7,8]]
result = Solution().findMinArrowShots(points)
assert result == 4

points = [[1,2],[2,3],[3,4],[4,5]]
result = Solution().findMinArrowShots(points)
assert result == 2

points = [[1,2]]
result = Solution().findMinArrowShots(points)
assert result == 1

points = [[2,3],[2,3]]
result = Solution().findMinArrowShots(points)
assert result == 1
