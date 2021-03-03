from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        "2 Pointer of 2Sum, Time: O(n^2)"
        "Use set"
        n = len(nums)
        if n < 3: return []
        nums.sort()

        def twoSum(nums, target):
            result = set()
            i, j = 0, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    result.add((nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j-= 1
            return result

        result = set()
        for i, num1 in enumerate(nums[:n-2]):
            for num2, num3 in twoSum(nums[i+1:], -num1):
                result.add((num1, num2, num3))
        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        "2 Pointer of 2Sum, Time: O(n^2), Space: O(1)"
        "No use set"
        "https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution"
        n = len(nums)
        if n < 3: return []
        nums.sort()
        ans = []
        for i in range(n-2):
            if nums[i] > 0: break # Since the nums is sorted, if first number is bigger than 0, it is impossible to have a sum of 0.
            if i > 0 and nums[i] == nums[i-1]: continue # Skip duplicate of num1
            # 2 pointer to find num2, num3 which add up to 0-num1
            l, r, target = i+1, n-1, -nums[i]
            while l < r:
                if nums[l] + nums[r] == target: 
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1 # Skip duplicate of num2
                    while l < r and nums[r] == nums[r-1]: r -= 1 # Skip duplicate of num3
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target: l += 1
                else: r -= 1
        return ans

nums = [-1,0,1,2,-1,-4]
result = Solution().threeSum(nums)
print(result) # [[-1,-1,2],[-1,0,1]]

nums = []
result = Solution().threeSum(nums)
print(result) # []

nums = [0]
result = Solution().threeSum(nums)
print(result) # []