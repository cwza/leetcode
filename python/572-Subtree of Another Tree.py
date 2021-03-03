from bintree_helper import *

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        "Time: O(mn)"
        def isSameTree(s, t):
            if s is None and t is None: return True
            if s and t: return s.val==t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            return False
        if s is None or t is None: return isSameTree(s, t)
        return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

s = deserialize("[3,4,5,1,2]")
t = deserialize("[4,1,2]")
ans = Solution().isSubtree(s, t)
assert ans==True

s = deserialize("[3,4,5,1,2,null,null,null,null,0]")
t = deserialize("[4,1,2]")
ans = Solution().isSubtree(s, t)
assert ans==False