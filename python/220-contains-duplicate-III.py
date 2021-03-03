from typing import List
from sortedcontainers import SortedSet


'''
https://www.youtube.com/watch?v=Cu7g9ovYHNI
follow up 219
'''


def find_floor_ceiling(s: SortedSet, num: int) :
    ''' floor: maximum value in s which is less than or equal to num 
        ceiling: minimum value in s which is larger than or equal to num '''
    if num in s:
        return num, num
    else:
        idx = s.bisect_left(num)
        floor = s[idx - 1] if idx - 1 >= 0 else None
        ceiling = s[idx] if idx < len(s) else None
    return floor, ceiling

s = SortedSet([2, 3, 6, 7, 8])
assert find_floor_ceiling(s, 5) == (3, 6)
assert find_floor_ceiling(s, 6) == (6, 6)
assert find_floor_ceiling(s, 10) == (8, None)
assert find_floor_ceiling(s, 1) == (None, 2)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        s = SortedSet()
        for i, num in enumerate(nums): # O(n)
            # print(s, num)
            floor, ceiling = find_floor_ceiling(s, num) # O(logk)
            # print(floor, ceiling)
            if floor is not None and num - floor <= t:
                return True
            if ceiling is not None and ceiling - num <= t:
                return True
            s.add(num)   
            if len(s) > k:
                s.remove(nums[i-k]) # O(logk)
        return False

nums = [1,2,3,1]
k = 3
t = 0
result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
assert result == True

nums = [1,0,1,1]
k = 1
t = 2
result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
assert result == True

nums = [1,5,9,1,5,9]
k = 2
t = 3
result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
assert result == False
