from typing import List

'''

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        "Counting Sort, Time: O(n), Space: O(n)"
        from collections import Counter
        counter = Counter(nums)
        i = 0
        for color in range(3):
            for _ in range(counter[color]):
                nums[i] = color 
                i += 1
    def sortColors(self, nums: List[int]) -> None:
        "Two Pointer, Time: O(n), Space: O(1)"
        "https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation"
        n = len(nums)
        l, r = 0, n-1
        cur = 0
        while cur <= r:
            if nums[cur] == 0: 
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            else: cur += 1

nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
assert nums == [0,0,1,1,2,2]

nums = [2,0,1]
Solution().sortColors(nums)
assert nums == [0,1,2]

nums = [0]
Solution().sortColors(nums)
assert nums == [0]

nums = [1]
Solution().sortColors(nums)
assert nums == [1]

nums = [1,2,0]
Solution().sortColors(nums)
assert nums == [0,1,2]