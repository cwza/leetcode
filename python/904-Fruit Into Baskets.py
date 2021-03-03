from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        "Sliding Window, Time: O(n), Space: O(1)"
        n = len(tree)
        counter = Counter()
        l, result = 0, 0
        for r in range(n):
            counter[tree[r]] += 1
            while len(counter) > 2:
                counter[tree[l]] -= 1
                if counter[tree[l]] <=0: del counter[tree[l]]
                l += 1
            result = max(result, r-l+1)
        return result

tree = [1,2,1]
result = Solution().totalFruit(tree)
assert result == 3

tree = [0,1,2,2]
result = Solution().totalFruit(tree)
assert result == 3

tree = [1,2,3,2,2]
result = Solution().totalFruit(tree)
assert result == 4

tree = [3,3,3,1,2,1,1,2,3,3,4]
result = Solution().totalFruit(tree)
assert result == 5