from typing import List

'''
Solution1:
  https://www.youtube.com/watch?v=nTKdYm_5-ZY
Solution2:
  Animation: https://www.youtube.com/watch?v=wDgKaNrSOEI
  With Math Proof: https://www.youtube.com/watch?v=rf66wlb9aNQ
'''
class Solution:
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     "Brute Force: O(n^2)"
    #     n = len(gas)
    #     for start in range(n):
    #         surplus = 0
    #         fail = False
    #         for j in range(start, start+n):
    #             j = j % n
    #             surplus = surplus + gas[j] - cost[j]
    #             if surplus < 0:
    #                 fail = True
    #                 break
    #         if not fail:
    #             return start
    #     return -1
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     "Solution1: O(n)"
    #     n = len(gas)
    #     start, surplus, deficit = 0, 0, 0
    #     for i in range(n):
    #         surplus = surplus + gas[i] - cost[i]
    #         if surplus < 0:
    #             deficit += surplus
    #             surplus = 0
    #             start = i + 1
    #     if surplus + deficit < 0:
    #         return -1
    #     else:
    #         return start
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        "Solution2: O(n)"
        n = len(gas)

        if (sum(gas) - sum(cost)) < 0:
            return -1

        start, j, surplus = 0, 0, 0
        while j < n:
            surplus = surplus + gas[j] - cost[j]
            if surplus < 0:
                start = j + 1
                j = start
                surplus = 0
            else:
                j += 1

        return start

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
result = Solution().canCompleteCircuit(gas, cost)
assert result == 3

gas  = [2,3,4]
cost = [3,4,3]
result = Solution().canCompleteCircuit(gas, cost)
assert result == -1


