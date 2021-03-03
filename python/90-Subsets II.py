from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]):
        """
        Just like 78 approach1, but
        if we have duplicate elements (5, 5), instead of treating them as two elements that are duplicate, 
        we can treat it as one special element 5, but this element has more than two choices: 
        you can either NOT put it into the subset, 
        or put ONE 5 into the subset, 
        or put TWO 5s into the subset. 
        Therefore, we are given an array (a1, a2, a3, ..., an) with each of them appearing (k1, k2, k3, ..., kn) times, the number of subset is (k1+1)(k2+1)...(kn+1). 
        """
        from collections import Counter
        counter = Counter(nums)
        nums = list(counter.keys())
        n = len(nums)
        ans = []
        def dfs(i, path: List):
            nonlocal nums
            if i == n: 
                ans.append(path[:])
                return
            for count in range(counter[nums[i]]+1): # count is the number of appears of nums[i]
                for _ in range(count): path.append(nums[i])
                dfs(i+1, path)
                for _ in range(count): path.pop()
        dfs(0, [])
        return ans
    # def subsetsWithDup(self, nums: List[int]):
    #     "Just like 78 approach 2, but add sort and if cur num is equal to previous num skip it"
    #     nums.sort()
    #     n = len(nums)
    #     result = []
    #     def dfs(i, path):
    #         result.append(path[:])
    #         prev = ""
    #         for j in range(i, n):
    #             if nums[j] == prev: continue # Skip 
    #             prev = nums[j]
    #             path.append(nums[j])
    #             dfs(j+1, path)
    #             path.pop()
    #     dfs(0, [])
    #     return result


nums = [1,2,2]
result = Solution().subsetsWithDup(nums)
print(result) # [[2],[1],[1,2,2],[2,2],[1,2],[]]

nums = [4,4,4,1,4]
result = Solution().subsetsWithDup(nums)
print(result) # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]