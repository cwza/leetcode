
'''
This is a tricky math problem.
https://leetcode.com/problems/smallest-integer-divisible-by-k/solution/

Ex: K = 3
1      % 3 = 1
11     % 3 = 2     <=>  11 % 3 = 2
111    % 3 = 0     <=>  21 % 3 = 0
1111   % 3 = 1     <=>  01 % 3 = 1
11111  % 3 = 2     <=>  11 % 3 = 2
111111 % 3 = 0     <=>  21 % 3 = 0
...
The remainder is repeated over and over. The repeated period is K.
If N can't be divide within N loop, then it is guranteed that the N is not exists.
N(2) = remainder of N(1) * 10 + 1
'''

class Solution:
    # def smallestRepunitDivByK(self, K: int) -> int:
    #     N = 0
    #     for result in range(1, K+1):
    #         N = N*10 + 1
    #         if N % K == 0:
    #             return result
    #     return -1
    def smallestRepunitDivByK(self, K: int) -> int:
        N = 0
        for result in range(1, K+1):
            N = N*10 + 1
            N = N % K
            if N % K == 0:
                return result
        return -1

K = 1
result = Solution().smallestRepunitDivByK(K)
assert result == 1

K = 2
result = Solution().smallestRepunitDivByK(K)
assert result == -1

K = 3
result = Solution().smallestRepunitDivByK(K)
assert result == 3