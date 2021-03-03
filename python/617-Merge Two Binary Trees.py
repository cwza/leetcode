from bintree_helper import *

class Solution:
    def mergeTrees(self, t1, t2) -> TreeNode:
        "DFS, Time: O(n), Space: O(n)"
        def dfs(t1, t2):
            if t1 is None: return t2
            if t2 is None: return t1
            t1.val += t2.val
            t1.left = dfs(t1.left, t2.left)
            t1.right = dfs(t1.right, t2.right)
            return t1
        return dfs(t1, t2)
    

t1 = deserialize("[1,3,2,5]")
t2 = deserialize("[2,1,3,null,4,null,7]")
result = Solution().mergeTrees(t1, t2)
drawtree(result)