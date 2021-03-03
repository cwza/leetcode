from bintree_helper import *

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        "2 nested DFS, Time: O(n^2)"
        if root is None: return 0
        def dfs(root, k):
            "returns number of paths add up to k from root include root"
            count = 0
            if root.val == k: count += 1
            if root.left: count += dfs(root.left, k-root.val)
            if root.right: count += dfs(root.right, k-root.val)
            return count
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        "Prefixsum, Time: O(n), Space: O(n)"
        "Concept is same as LeetCode 560"
        "https://www.youtube.com/watch?v=uZzvivFkgtM"
        if root is None: return 0
        from collections import Counter
        result = 0
        prefixsum = Counter()
        def dfs(root, running_sum):
            nonlocal result
            running_sum += root.val
            if running_sum == sum: result += 1
            result += prefixsum[running_sum-sum]
            prefixsum[running_sum] += 1
            if root.left:
                dfs(root.left, running_sum)
            if root.right:
                dfs(root.right, running_sum)
            prefixsum[running_sum] -= 1
        dfs(root, 0)
        return result

root = deserialize("[10,5,-3,3,2,null,11,3,-2,null,1]")
sum = 8
result = Solution().pathSum(root, sum)
assert result == 3

root = deserialize("[1,-2,-3,1,3,-2,null,-1]")
sum = -1
result = Solution().pathSum(root, sum)
assert result == 4