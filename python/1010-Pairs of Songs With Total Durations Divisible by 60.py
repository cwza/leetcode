from typing import List
from collections import Counter, defaultdict

'''
Using Modulo Distributive Law:
(a+b) % 60 = 0 => ((a % 60)+(b % 60)) % 60 = 0
Therefore, either  
1. a % 60 = 0 and b % 60 = 0 or
2. (a % 60) + (b % 60) = 60

So we want to find b such that:
1. b % 60 = 0, if a % 60 = 0
2. b % 60 = 60−(a % 60), if a % 60 != 0
'''

class Solution:
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     "Brute Force, Time: O(n^2), Space: O(1), TLE"
    #     n = len(time)
    #     result = 0
    #     for i in range(0, n-1):
    #         for j in range(i+1, n):
    #             if (time[i] + time[j]) % 60 == 0: 
    #                 result += 1
    #     return result
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     "Time: O(16n), Space: O(n+16)"
    #     multiples = [i*60 for i in range(1, 17)]
    #     counter = Counter()
    #     result = 0
    #     for t in time:
    #         for multiply in multiples:
    #             remain = multiply - t
    #             if counter[remain] > 0:
    #                 result += counter[remain]
    #         counter[t] += 1
    #     return result
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        "Math, Modulo Property, Time: O(n), Space: O(60)"
        remainders = defaultdict(list) # {remainder: [t]}, ex: {0: [60], 30: [30, 50], 40: [100, 40], 20: [80]}
        result = 0
        for a in time:
            if a % 60 == 0:
                result += len(remainders[0])
            else:
                result += len(remainders[60 - (a % 60)])
            remainders[a%60].append(a)
        return result

time = [30,20,150,100,40]
result = Solution().numPairsDivisibleBy60(time)
assert result == 3

time = [60,60,60]
result = Solution().numPairsDivisibleBy60(time)
assert result == 3