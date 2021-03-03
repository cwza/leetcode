from typing import List

'''
Space: O(1)
This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.
Algs:
1. reverse nums
2. reverse first k elements
3. reverse last n-k elemnts

ex1:
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
1.     [7, 6, 5, 4, 3, 2, 1]
2.     [5, 6, 7, 4, 3, 2, 1]
3.     [5, 6, 7, 1, 2, 3, 4]

ex2:
nums = [   -1, -100,    3,   99], k = 2
1.     [   99,    3, -100,   -1]
2.     [    3,   99, -100,   -1]
3.     [    3,   99,   -1, -100]
'''

class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     "Time: O(n), Space: O(n)"
    #     ori_nums = nums[:]
    #     n = len(nums)
    #     k = k % n
    #     for i, num in enumerate(ori_nums):
    #         nums[(i+k)%n] = num
    def rotate(self, nums: List[int], k: int) -> None:
        "Time: O(n), Space: O(1)"
        def inplace_reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k = k % n
        inplace_reverse(nums, 0, n-1)
        inplace_reverse(nums, 0, k-1)
        inplace_reverse(nums, k, n-1)

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
assert nums == [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
assert nums == [3,99,-1,-100]




        