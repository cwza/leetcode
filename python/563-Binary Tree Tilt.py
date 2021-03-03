from bintree_helper import *

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        "Post-Order traversal, Time: O(n), Time: O(n)"
        self.result = 0
        def post_order(root):
            "return the sum of all nodes and add the sum to the result variable"
            if root is None:
                return 0
            left_sum = post_order(root.left)
            right_sum = post_order(root.right)
            self.result += abs(left_sum-right_sum)
            return left_sum+right_sum+root.val
        post_order(root)
        return self.result

root = deserialize("[1,2,3]")
result = Solution().findTilt(root)
assert result == 1

root = deserialize("[4,2,9,3,5,null,7]")
result = Solution().findTilt(root)
assert result == 15

root = deserialize("[21,7,14,1,1,2,2,3,3]")
result = Solution().findTilt(root)
assert result == 9
