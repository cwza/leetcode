from bintree_helper import *
from functools import lru_cache
from collections import deque, defaultdict

'''
Down-Top DP
How to map integer to tree node????
We need an array to represent each node. We use the BFS order to represent it.
    3
  2   7
1   5    4
tree: [3, 2, 7, 1, 5, 4]
ex: tree[0]: root node, tree[5]: most right-down node, ...etc

We also need to store the parent-children relation. We use graph to store it.
graph: {-1:[3], 0:[1, 2], 1:[3, 4], 2:[5] }

i: BFS order index of a node
dp_rob[i]: max amount of steal if start from node i and i is robbed
dp_not_rob[i]: max amount of steal if start from node i and i is not robbed

Base case:
leaf: at tree array right most
dp_rob[leaf] = tree[leaf]
dp_not_rob[leaf] = 0

Transition function:
left child of i = graph[i][0], right child of i = graph[i][1]
dp_rob[i] = tree[i] + dp_not_rob[left child of i] + dp_not_rob[right child of i]
dp_not_rob[i] = max(dp_rob[left child of i], dp_not_rob[left child of i]) + max(dp_rob[right child of i], dp_not_rob[right child of i])

Iterate:
Our tree array is in BFS order, right in array always means down in tree, so we can fill out the tree array from right to left.

Result:
max(dp_rob[0], dp_not_rob[0])
'''

class Solution:
    # def rob(self, root: TreeNode) -> int:
    #     "Time: O(n), Space: O(n)"
    #     @lru_cache(None)
    #     def helper(root, is_parent_rob):
    #         "return max amount of root if its parent is rob or not by is_parent_rob"
    #         if root is None: return 0
    #         if is_parent_rob:
    #             return helper(root.left, False) + helper(root.right, False)
    #         else:
    #             notrob = helper(root.left, False) + helper(root.right, False)
    #             rob = root.val + helper(root.left, True) + helper(root.right, True)
    #             return max(rob, notrob)
    #     return helper(root, False)
    def rob(self, root: TreeNode) -> int:
        "Down-Top DP: Time: O(n), Space: O(n)"
        if root is None: return 0

        ## Run BFS to build the tree and graph
        queue = deque()
        queue.append((root, -1)) # node, parent_idx
        tree = []
        graph = defaultdict(list)
        idx = 0
        while queue:
            node, parent_idx = queue.popleft()
            tree.append(node.val)
            graph[parent_idx].append(idx)
            if node.left is not None: queue.append((node.left, idx))
            if node.right is not None: queue.append((node.right, idx))
            idx += 1
        print(tree, graph)

        ## Run DP
        n = len(tree)
        dp_rob = [0 for _ in range(n)]
        dp_not_rob = dp_rob[:]
        for i in reversed(range(n)):
            if i not in graph or len(graph[i]) == 0: # Leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                child_idxs = graph[i]
                # dp_rob[i] = tree[i] + dp_not_rob[left_child_idx] + dp_not_rob[right_child_idx]
                dp_rob[i] = tree[i] + sum([dp_not_rob[child_idx] for child_idx in child_idxs])
                # dp_not_rob[i] = max(dp_rob[left_child_idx], dp_not_rob[left_child_idx]) + max(dp_rob[right_child_idx], dp_not_rob[right_child_idx])
                dp_not_rob[i] = sum([max(dp_rob[child_idx], dp_not_rob[child_idx]) for child_idx in child_idxs])

        return max(dp_rob[0], dp_not_rob[0])

root = deserialize("[3,2,3,null,3,null,1]")
result = Solution().rob(root)
assert result == 7

root = deserialize("[3,4,5,1,3,null,1]")
result = Solution().rob(root)
assert result == 9