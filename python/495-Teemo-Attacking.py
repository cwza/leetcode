from typing import List

'''
Very similar to 56
'''


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        "O(n)"
        if len(timeSeries) == 0 or duration == 0: return 0

        result = 0
        for i in range(len(timeSeries)-1):
            result += min(timeSeries[i+1] - timeSeries[i], duration)
        result += duration
        return result
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    #     "O(n): Use the result of 56-merge-intervals"
    #     def gen_merged_list(intervals):
    #         "code from 56"
    #         result = [intervals[0]]
    #         for i in range(1, len(intervals)):
    #             a = result[-1]
    #             b = intervals[i]
    #             if a[1] >= b[0]:
    #                 merged = [a[0], max(a[1], b[1])]
    #                 result.pop()
    #                 result.append(merged)
    #             else:
    #                 result.append(b)
    #         return result
    
    #     if len(timeSeries) == 0 or duration == 0: return 0

    #     intervals = [[t, t+duration] for t in timeSeries]
    #     merged_list = gen_merged_list(intervals)
    #     result = 0
    #     for interval in merged_list:
    #         result += interval[1] - interval[0]
    #     return result


timeSeries = [1,4]
duration = 2
result = Solution().findPoisonedDuration(timeSeries, duration)
assert result == 4

timeSeries = [1,2]
duration = 2
result = Solution().findPoisonedDuration(timeSeries, duration)
assert result == 3