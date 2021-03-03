from bintree_helper import *
from collections import deque

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(node):
            if node is None: return 'X'
            ser_left = helper(node.left)
            ser_right = helper(node.right)
            return f'{node.val},{ser_left},{ser_right}'
        return helper(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes_left = deque(data.split(','))
        def helper(nodes_left):
            "return a tree that use nodes_left[0] as root, and put all other nodes that can not use nodes_left[0] as root left at nodes_left"
            if not nodes_left: return None
            val = nodes_left.popleft()
            if val == "X": return None
            node = TreeNode(int(val))
            node.left = helper(nodes_left)
            node.right = helper(nodes_left)
            return node
        result = helper(nodes_left)
        return result
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

root = deserialize("[1,2,3,null,null,4,5,null,null,null,null]")
ser = Codec().serialize(root)
des = Codec().deserialize(ser)
drawtree(des)