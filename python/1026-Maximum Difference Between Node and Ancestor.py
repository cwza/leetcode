from bintree_helper import *

'''
Post-Order:
post_order(root): 
'''

class Solution:
    # def maxAncestorDiff(self, root: TreeNode) -> int:
    #     "Post-Order, Time: O(n), Space: O(n) [max stack size]"
    #     self.result = 0
    #     def post_order(root):
    #         "returns min value and max value in the tree start with root"
    #         if root is None:
    #             return float("+inf"), float("-inf")
    #         if root.left is None and root.right is None:
    #             return root.val, root.val
    #         left_min, left_max = post_order(root.left)
    #         right_min, right_max = post_order(root.right)
    #         min_cur = min(left_min, right_min)
    #         max_cur = max(left_max, right_max)
    #         self.result = max(self.result, abs(root.val-min_cur), abs(root.val-max_cur))
    #         return min(root.val, min_cur), max(root.val, max_cur)
    #     post_order(root)
    #     return self.result
    def maxAncestorDiff(self, root: TreeNode) -> int:
        "Pre-Order, Time: O(n), Space: O(n)"
        self.result = 0
        def pre_order(node, min_cur, max_cur):
            "min_cur: the min value from root to node, max_cur: the max value from root to node"
            if node is None:
                return
            self.result = max(self.result, abs(node.val-min_cur), abs(node.val-max_cur))
            min_cur = min(node.val, min_cur)
            max_cur = max(node.val, max_cur)
            pre_order(node.left, min_cur, max_cur)
            pre_order(node.right, min_cur, max_cur)
        pre_order(root, root.val, root.val)
        return self.result

root = deserialize("[8,3,10,1,6,null,14,null,null,4,7,13]")
result = Solution().maxAncestorDiff(root)
assert result == 7

root = deserialize("[1,null,2,null,0,3]")
result = Solution().maxAncestorDiff(root)
assert result == 3