from bintree_helper import *

'''
We need to find the two node and swap their value
Key: In-order traversal on BST will produce a sorted list!!!!!
     10
   5    15      => [4, 5, 7, 10, 14, 15, 17]
  4 7  14 17

Ex:
     10
   15    5      => nodes = [4, 15, 7, 10, 14, 5, 17]
  4 7  14 17

First Solution:
1. In-order traversal and save them to an array
2. One-Pass to Find the value which are in [large, small] order i.e.: [15, 7], [14, 5]
3. The 2 nodes are the 15 and 5 which is the left in first list and right in second list 
4. Swap their value
5. Special case: if we only find one such list ex: [2, 4, 3, 5, 6] => [4, 3], then we just swap them

first, second = None, None # The two nodes that need to be swapped
for i = 1 ~ n:
    if nodes[i].val < nodes[i-1].val:
        if first is None: first = nodes[i-1]
        second = nodes[i]
first.val, second.val = second.val, first.val


Second Solution:
We can do this without an extra array.
Key: When we do in-order traversal, we can store a prev node which is the left of the current node
     ex: cur: 15 => prev: 4, cur: 7 => prev: 15, cur: 10 => prev: 7

in_order(cur.left)
if prev and cur.val < prev.val
    if first is None: first = prev
    second = cur
prev = cur
in_order(cur.right)
'''

class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    #     "First Solution, Time: O(2n), Space: O(n)"
    #     # Store the in-order in array
    #     nodes = []
    #     def in_order(cur):
    #         if cur is None: return
    #         in_order(cur.left)
    #         nodes.append(cur)
    #         in_order(cur.right)
    #     in_order(root)

    #     # One-Pass the array to find the 2 nodes
    #     first, second = None, None
    #     for i in range(1, len(nodes)):
    #         if nodes[i].val < nodes[i-1].val:
    #             if first is None: first = nodes[i-1]
    #             second = nodes[i]
    #     first.val, second.val = second.val, first.val
    def recoverTree(self, root: TreeNode) -> None:
        "Second Solution, Time: O(2n), Space: O(n) for recursive stack"
        self.first, self.second, self.prev = None, None, None
        def in_order(cur):
            if cur is None: return
            in_order(cur.left)
            if self.prev is not None and cur.val < self.prev.val:
                if self.first is None: self.first = self.prev
                self.second = cur
            self.prev = cur
            in_order(cur.right)
        in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

# root = deserialize("[1,3,null,null,2]")
# Solution().recoverTree(root)
# drawtree(root)

root = deserialize("[3,1,4,null,null,2]")
Solution().recoverTree(root)
drawtree(root)