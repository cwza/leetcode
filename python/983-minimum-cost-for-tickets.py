from typing import List

# https://www.youtube.com/watch?v=on7MoPbgefk
class Solution:
    def helper(self, i):
        if i <= 0: return 0
        if i in self.memo: return self.memo[i]

        if i not in self.days: return self.helper(i-1)

        pass1 = self.helper(i-1) + self.costs[0]
        pass2 = self.helper(i-7) + self.costs[1]
        pass3 = self.helper(i-30) + self.costs[2]
        result = min(pass1, pass2, pass3)
        self.memo[i] = result
        return result
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = set(days)
        self.costs = costs
        self.memo = {}

        result = self.helper(days[-1])
        return result

# days = [1,4,6,7,8,20]
# costs = [2,7,15]
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(Solution().mincostTickets(days, costs))