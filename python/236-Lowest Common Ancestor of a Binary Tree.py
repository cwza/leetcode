from bintree_helper import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        "Approach2 Find by Parent, Time: O(n), Space: O(n)"
        # Generate parent
        parent = {root: None}
        def dfs(root):
            if p in parent and q in parent: return 
            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)
        dfs(root)
        # Find LCA by parent
        p_parents = set()
        while p: # Store all parents of p
            p_parents.add(p)
            p = parent[p]
        while q: # The first parent that also appears in p_parents is the LCA
            if q in p_parents:
                return q
            q = parent[q]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        "Approach1 Recursive, Time: O(n), Space: O(n)"
        "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/"
        ans = None
        def dfs(root):
            "return whether has p or q"
            nonlocal ans
            l, r = False, False
            if root.left: l = dfs(root.left)
            if root.right: r = dfs(root.right)
            m = root == p or root == q
            if m:
                if l or r:
                    ans = root
                return True
            if not m:
                if l and r:
                    ans = root
                if not l and not r:
                    return False
                return True
        dfs(root)
        return ans

root = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
p = root.left # 5
q = root.right # 1
result = Solution().lowestCommonAncestor(root, p, q)
assert result.val == 3

root = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
p = root.left # 5
q = root.left.right.right # 4
result = Solution().lowestCommonAncestor(root, p, q)
assert result.val == 5

root = deserialize("[1,2]")
p = root # 1
q = root.left # 2
result = Solution().lowestCommonAncestor(root, p, q)
assert result.val == 1
