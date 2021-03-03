
'''
A binary number plus its complement will equal 111....111 in binary.
Also, N = 0 is a corner case.
'''

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_n = bin(N)[2:]
        decimal_ones = 2**len(bin_n) - 1
        return decimal_ones - N

N = 5
result = Solution().bitwiseComplement(N)
assert result == 2

N = 7
result = Solution().bitwiseComplement(N)
assert result == 0

N = 10
result = Solution().bitwiseComplement(N)
assert result == 5