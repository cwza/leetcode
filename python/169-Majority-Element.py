from typing import List
from collections import Counter

'''
https://www.cnblogs.com/grandyang/p/4233501.html
Moore Voting
Time: O(n)
Space: O(1)
'''

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     "Use hash, so space: O(n)"
    #     counter = Counter(nums)
    #     return counter.most_common(1)[0][0]
    def majorityElement(self, nums: List[int]) -> int:
        "Use Moore Voting, so space: O(1)"
        res, cnt = -1, 0
        for num in nums:
            if num == res:
                cnt += 1
            else:
                if cnt == 0:
                    res = num
                    cnt = 1
                elif cnt > 0:
                    cnt -= 1
                else:
                    raise Exception('Suck!!!')
        return res

nums = [3,2,3]
result = Solution().majorityElement(nums)
assert result == 3

nums = [2,2,1,1,1,2,2]
result = Solution().majorityElement(nums)
assert result == 2
