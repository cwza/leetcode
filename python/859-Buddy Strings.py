'''
Consider 4 conditions:
1. No difference: True if s contains duplicated chars else False
2. 1 difference: False
3. 2 diffrence: Check if we can swap this 2 diffrence position to get the same string
4. > 2 difference: Fasle
'''

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        "Greedy, Time: O(len(A)), Space: O(1)"
        if len(A) != len(B): return False
        num_diff = 0
        diff_idx = []
        for i in range(len(A)):
            if num_diff > 2:
                return False
            if A[i] != B[i]:
                num_diff += 1
                diff_idx.append(i)
        if num_diff == 0:
            return len(set(A)) < len(A)
        elif num_diff == 1:
            return False
        elif num_diff == 2:
            return A[diff_idx[0]] == B[diff_idx[1]] and A[diff_idx[1]] == B[diff_idx[0]]

A = "ab"
B = "ba"
result = Solution().buddyStrings(A, B)
assert result == True

A = "ab"
B = "ab"
result = Solution().buddyStrings(A, B)
assert result == False

A = "aa"
B = "aa"
result = Solution().buddyStrings(A, B)
assert result == True

A = "aaaaaaabc"
B = "aaaaaaacb"
result = Solution().buddyStrings(A, B)
assert result == True

A = ""
B = "aa"
result = Solution().buddyStrings(A, B)
assert result == False
