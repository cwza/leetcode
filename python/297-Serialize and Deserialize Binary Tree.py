from bintree_helper import *
from collections import deque

"Time: O(n), Space: O(n)"
# class Codec:
#     "Pre-Order"
#     def serialize(self, root):
#         result = []
#         def helper(node):
#             if node is None: 
#                 result.append("#")
#                 return
#             result.append(str(node.val))
#             helper(node.left)
#             helper(node.right)
#         helper(root)
#         return ",".join(result)

#     def deserialize(self, data):
#         data = deque(data.split(','))
#         def helper(data):
#             if len(data) == 0: return
#             val = data.popleft()
#             if val == '#':
#                 return None
#             node = TreeNode(int(val))
#             node.left = helper(data)
#             node.right = helper(data)
#             return node
#         return helper(data)

class Codec:
    "BFS-Order"
    def serialize(self, root):
        if root is None: return "#"
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)

    def deserialize(self, data):
        data_q = deque(data.split(','))
        root_val = data_q.popleft()
        if root_val == "#": return None
        root_node = TreeNode(root_val)
        node_q = deque([root_node])
        while node_q:
            node = node_q.popleft()
            left_val = data_q.popleft()
            if left_val == "#":
                node.left = None
            else:
                node.left = TreeNode(left_val)
                node_q.append(node.left)
            right_val = data_q.popleft()
            if right_val == "#":
                node.right = None
            else:
                node.right = TreeNode(right_val)
                node_q.append(node.right)
        return root_node

root = deserialize("[1,2,3,null,null,4,5]")
serialized = Codec().serialize(root)
print(serialized)
deserialized = Codec().deserialize(serialized)
drawtree(deserialized)