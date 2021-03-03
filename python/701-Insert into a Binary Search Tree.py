from bintree_helper import *

class Solution:
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     "Recursive"
    #     if root is None: return TreeNode(val)
    #     def helper(cur_node):
    #         if val < cur_node.val:
    #             if cur_node.left is None:
    #                 cur_node.left = TreeNode(val)
    #                 return
    #             else:
    #                 helper(cur_node.left)
    #         else:
    #             if cur_node.right is None:
    #                 cur_node.right = TreeNode(val)
    #                 return
    #             else:
    #                 helper(cur_node.right)
    #     helper(root)
    #     return root
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        "Loop"
        if root is None: return TreeNode(val)
        cur_node = root
        while True:
            if val < cur_node.val:
                if cur_node.left is None:
                    cur_node.left = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.right
        return root

# root = deserialize("[4,2,7,1,3]")
# val = 5
# result = Solution().insertIntoBST(root, val)
# drawtree(result)

# root = deserialize("[40,20,60,10,30,50,70]")
# val = 25
# result = Solution().insertIntoBST(root, val)
# drawtree(result)

root = deserialize("[4,2,7,1,3,null,null,null,null,null,null]")
val = 5
result = Solution().insertIntoBST(root, val)
drawtree(result)

