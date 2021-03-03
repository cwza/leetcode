class Solution:
    def allUniqueSplit(self, s):
        result = []
        table = {}
        def helper(path, remains):
            if len(remains) == 0:
                result.append(path)
            for i in range(1, len(remains)+1):
                tmp = remains[:i]
                if tmp in table:
                    continue
                table[tmp] = 1
                helper(path[:]+[tmp], remains[i:])
                del table[tmp]
        helper([], s)
        return result
    def maxUniqueSplit(self, s: str) -> int:
        if len(s) == 0: return 0
        table = {}
        def helper(remains):
            if len(remains) == 0:
                return 0
            result = 0
            for i in range(1, len(remains)+1):
                tmp = remains[:i]
                if tmp in table:
                    continue
                table[tmp] = 1
                result = max( result, 1 + helper(remains[i:]) )
                del table[tmp]
            return result
        return helper(s)

s = "ababccc"
result = Solution().maxUniqueSplit(s)
assert result == 5

s = "aba"
result = Solution().maxUniqueSplit(s)
assert result == 2

s = "aa"
result = Solution().maxUniqueSplit(s)
assert result == 1