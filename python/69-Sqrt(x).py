class Solution:
    def mySqrt(self, x: int) -> int:
        "Binary Search, Time: O(logx), Space: O(1)"
        if x == 1: return 1
        l, r = 1, x+1
        while l < r:
            m = l + (r-l)//2
            if m**2 > x: r = m
            else: l = m + 1
        return l - 1

x = 4
result = Solution().mySqrt(x)
assert result == 2

x = 8
result = Solution().mySqrt(x)
assert result == 2
