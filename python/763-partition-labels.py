from typing import List

'''
https://www.cnblogs.com/grandyang/p/8654822.html
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_table = {ch: i for i, ch in enumerate(S)}
        result = []
        start, last = 0, 0
        for i in range(len(S)):
            last = max(last, last_table[S[i]])
            if i == last:
                result.append(last-start+1)
                start = last + 1
        return result

S = "ababcbacadefegdehijhklij"
result = Solution().partitionLabels(S)
assert result == [9,7,8]