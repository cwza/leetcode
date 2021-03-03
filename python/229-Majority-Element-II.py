from typing import List
from collections import Counter

'''
https://www.cnblogs.com/grandyang/p/4606822.html
Moore Voting
Time: O(n)
Space: O(1)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        "Use Moore Voting, so space: O(1)"
        res1, cnt1, res2, cnt2 = -1, 0, -1, 0

        # 1. Find first 2 most common elements (Majority candidates)
        for num in nums:
            if num == res1:
                cnt1 += 1
            elif num == res2:
                cnt2 += 1
            elif cnt1 == 0:
                res1 = num
                cnt1 = 1
            elif cnt2 == 0:
                res2 = num
                cnt2 = 1
            elif cnt1 > 0 and cnt1 > 0:
                cnt1 -= 1
                cnt2 -= 1
            else:
                raise Exception('Suck!!!!')
        
        # 2. Check whether these 2 candidates really appear more than n//3 times
        res1_appears, res2_appears = 0, 0
        for num in nums:
            if num == res1:
                res1_appears += 1
            if num == res2:
                res2_appears += 1
        results = []
        if res1_appears > len(nums)//3:
            results.append(res1)
        if res2_appears > len(nums)//3:
            results.append(res2)
        
        return results
    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     "Use hash, so space: O(n)"
    #     counter = Counter(nums)
    #     return [key for key, val in counter.items() if val > len(nums)//3]

nums = [3,2,3]
result = Solution().majorityElement(nums)
assert result == [3]

nums = [1,1,1,3,3,2,2,2]
result = Solution().majorityElement(nums)
assert result == [1, 2]