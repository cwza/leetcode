from bintree_helper import *
from typing import List

'''
The basic idea is here:
Say we have 2 arrays, PRE and IN.
Preorder traversing implies that PRE[0] is the root node.
Then we can find this PRE[0] in IN, say it's IN[5].
Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
Recursively doing this on subarrays, we can build a tree out of it :)

https://www.cnblogs.com/grandyang/p/4296500.html
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) <= 0: return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)
        preorder.pop(0)
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx+1:])
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        table = {num: i for i, num in enumerate(inorder)} # pos map
        def helper(pre_start, in_start, in_end):
            if in_end < in_start: return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_idx = table[root_val]
            root.left = helper(pre_start+1, in_start, root_idx-1)
            root.right = helper(pre_start+root_idx-in_start+1, root_idx+1, in_end)
            return root
        return helper(0, 0, len(inorder)-1)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
result = Solution().buildTree(preorder, inorder)
drawtree(result)