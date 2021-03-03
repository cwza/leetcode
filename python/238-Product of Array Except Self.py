from typing import List

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     "Precompute L, R product, Time: O(n), Space: O(n)"
    #     n = len(nums)
    #     # L[i]: product of nums[0, i-1]
    #     L = [1]*n
    #     for i in range(1, n):
    #         L[i] = L[i-1] * nums[i-1]
    #     # R[i]: product of nums[i+1, n]
    #     R = [1]*n
    #     for i in reversed(range(n-1)):
    #         R[i] = R[i+1] * nums[i+1]
    #     # print(L, R)

    #     result = [1]*n
    #     for i in range(n):
    #         result[i] = L[i] * R[i]
    #     return result
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        "Use output list as R and Compute L on the fly, Time: O(n), Space: O(1) exclude space used by output"
        n = len(nums)
        R = [1]*n # This is also be used as result list
        for i in reversed(range(n-1)):
            R[i] = R[i+1] * nums[i+1]
        
        cur_L = 1
        for i in range(n):
            R[i] = cur_L * R[i]
            cur_L = cur_L * nums[i]
        return R

nums = [2,3,4,5]
result = Solution().productExceptSelf(nums)
assert result == [60,40,30,24]

nums = [2,3,0,5]
result = Solution().productExceptSelf(nums)
assert result == [0,0,30,0]