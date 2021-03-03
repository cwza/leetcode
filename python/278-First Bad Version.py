def create_isBadVersion(bad):
    def isBadVersion(version):
        if version >= bad: return True
        else: return False
    return isBadVersion
isBadVersion = create_isBadVersion(bad=4)

class Solution:
    def firstBadVersion(self, n):
        "Binary Search, Time: O(logn), Space: O(1)"
        l, r = 1, n+1
        while l < r:
            m = l + (r-l)//2
            if isBadVersion(m): r = m
            else: l = m + 1
        if l == n+1: return -1
        return l

result = Solution().firstBadVersion(5)
assert result == 4