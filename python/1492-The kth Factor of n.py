
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        "Brute Force, Time: O(n), Space: O(1)"
        cnt = 0
        result = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
                result = i
                if cnt == k:
                    return result
        return -1

n = 12
k = 3
result = Solution().kthFactor(n, k)
assert result == 3

n = 7
k = 2
result = Solution().kthFactor(n, k)
assert result == 7

n = 4
k = 4
result = Solution().kthFactor(n, k)
assert result == -1

n = 1
k = 1
result = Solution().kthFactor(n, k)
assert result == 1

n = 1000
k = 3
result = Solution().kthFactor(n, k)
assert result == 4
