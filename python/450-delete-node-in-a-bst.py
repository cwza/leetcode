from bintree_helper import TreeNode, deserialize, drawtree
'''
https://www.youtube.com/watch?v=gcULXE7ViZw
'''
class Solution:
    def findMin(self, root):
        if root is None: return None
        while root.left is not None:
            root = root.left
        return root
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None: return root
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
            return root
        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
            return root
        
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            right_min_node = self.findMin(root.right)
            root.val = right_min_node.val
            root.right = self.deleteNode(root.right, root.val)
            return root

tree = '[5,3,6,2,4,null,7]'
root = deserialize(tree)
solution = Solution()
result = solution.deleteNode(root, 3)
drawtree(result)