from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # Monotonic Decreasing Deque, Time: O(n), Space: O(n)
        from collections import deque;
        d = deque() # We store idx in deque, the values are decreasing
        n = len(T)
        ans = [0]*n
        for i in reversed(range(n)):
            while(d and T[d[-1]] <= T[i]): d.pop()
            if(d): ans[i] = d[-1] - i
            else: ans[i] = 0
            d.append(i)
        return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
ans = Solution().dailyTemperatures(T)
assert ans == [1, 1, 4, 2, 1, 1, 0, 0]