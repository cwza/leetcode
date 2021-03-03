from typing import List
from collections import Counter

class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     "Counter, Time: O(2n), Space: O(n)"
    #     n = len(s)
    #     if n < 10: return []
    #     counter = Counter()
    #     for i in range(0, n-9):
    #         sub_str = s[i:i+10]
    #         counter[sub_str] += 1
    #     results = [key for key, val in counter.items() if val > 1]
    #     return results
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        "2 Hash Set, Time: O(n), Space: O(2n)"
        n = len(s)
        if n < 10: return []
        check_repeat = set()
        result = set()
        for i in range(0, n-9):
            sub_str = s[i:i+10]
            if sub_str in check_repeat:
                result.add(sub_str)
            else:
                check_repeat.add(sub_str)
        return result

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = Solution().findRepeatedDnaSequences(s)
assert result == ["AAAAACCCCC","CCCCCAAAAA"]

s = "AAAAAAAAAAAAA"
result = Solution().findRepeatedDnaSequences(s)
assert result == ["AAAAAAAAAA"]

s = "AAAAAAAAAAA"
result = Solution().findRepeatedDnaSequences(s)
assert result == ["AAAAAAAAAA"]