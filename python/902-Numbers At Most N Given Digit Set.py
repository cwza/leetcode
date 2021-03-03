from typing import List

class Solution:
    # def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
    #     "Backtracking, Time: O(x^y), Space: O(y), x=len(digits), y=len(n)"
    #     "This results TLE"
    #     self.count = -1
    #     def backtrack(result):
    #         if result > n:
    #             return
    #         self.count += 1
    #         for digit in digits:
    #             digit = int(digit)
    #             backtrack(result * 10+ digit)
    #     backtrack(0)
    #     return self.count
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        "Math + Backtracking"
        "https://www.youtube.com/watch?v=d2O_jwPxroc"
        ns = [int(i) for i in str(n)]
        digits = [int(i) for i in digits]

        self.result = 0
        # 1 ~ n-1 位數, All posibility < n, Easy case use math
        for i in range(1, len(ns)):
            self.result += len(digits)**i
        
        # For the nth 位數
        def backtrack(pos):
            if pos == len(ns) - 1:
                self.result += sum([1 for digit in digits if digit <= ns[pos]])
                return
            leader_int = ns[pos]
            for digit in digits:
                if digit > leader_int:
                    return
                # Easy case use math
                elif digit < leader_int:
                    self.result += len(digits)**(len(ns)-pos-1)
                # Hard case, digit == leader_int, Recursive
                else:
                    backtrack(pos+1)
        backtrack(0)

        return self.result

digits = ["1","3","5","7"]
n = 100
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 20

digits = ["1","4","9"]
n = 1000000000
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 29523

digits = ["7"]
n = 8
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 1

digits = ["3","4","8"]
n = 4
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 2

digits = ["5","7","8"]
n = 59
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 6

digits = ["1"]
n = 834
result = Solution().atMostNGivenDigitSet(digits, n)
assert result == 3