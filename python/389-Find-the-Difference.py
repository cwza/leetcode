from collections import Counter

'''
Like 136, Use properties of XOR
* 任何數與0作xor運算結果不變, ex: 3 ^ 0 = 3
* 任何數與自己作xor運算結果為0, ex: 3 ^ 3 = 0
* xor運算有交換律, ex: 1 ^ 2 ^ 3 ^ 4 = 3 ^ 1 ^ 2 ^ 4 = 4 ^ 3 ^ 2 ^ 1
'''

class Solution:
    # def findTheDifference(self, s: str, t: str) -> str:
    #     "Hash, time: O(n), space: O(26), n is len(s) + len(t)"
    #     counter = Counter(s)
    #     for ch in t:
    #         if counter[ch] > 0:
    #             counter[ch] -= 1
    #         else:
    #             return ch
    #     return ""
    # def findTheDifference(self, s: str, t: str) -> str:
    #     "Diffrence of 2 Counter, oneline"
    #     return list((Counter(t) - Counter(s)).keys())[0]
    def findTheDifference(self, s: str, t: str) -> str:
        "Properties of XOR, time: O(n), space: O(1), n is len(s) + len(t)"
        res = 0
        for ch in s:
            res ^= ord(ch)
        for ch in t:
            res ^= ord(ch)
        return chr(res)

s = "abcd"
t = "abcde"
result = Solution().findTheDifference(s, t)
assert result == "e"