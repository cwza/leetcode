from bintree_helper import *

class Solution:
    # def increasingBST(self, root):
    #     "Store in-order sequence then relink, Time: O(n), Space: O(n)"
    #     order_arr = [] # in_order ordering of nodes
    #     def in_order(node):
    #         if node is None: return
    #         in_order(node.left)
    #         order_arr.append(node)
    #         in_order(node.right)
    #     in_order(root)
    #     dummy = TreeNode(0)
    #     cur = dummy
    #     for node in order_arr:
    #         node.left, node.right = None, None
    #         cur.right = node
    #         cur = node
    #     return order_arr[0]
    def increasingBST(self, root):
        "Relink nodes while in_order, Time: O(n), Space: O(1)"
        dummy = TreeNode(0)
        cur = dummy # The most right node of current result
        def in_order(node):
            "Properly order the node add them after cur and change cur to node"
            if node is None: return
            nonlocal cur
            in_order(node.left)
            node.left = None
            cur.right = node
            cur = node
            in_order(node.right)
        in_order(root)
        return dummy.right

root = deserialize("[5,3,6,2,4,null,8,1,null,null,null,7,9]")
result = Solution().increasingBST(root)
# drawtree(result)

root = deserialize("[5,1,7]")
result = Solution().increasingBST(root)
# drawtree(result)