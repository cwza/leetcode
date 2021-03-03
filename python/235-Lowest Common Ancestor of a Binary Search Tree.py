from bintree_helper import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        "Time: O(h), Space: O(1)"
        if p.val > q.val:
            p, q = q, p
        cur = root
        while cur:
            if p.val <= cur.val <= q.val:
                return cur
            if cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right
        return None

