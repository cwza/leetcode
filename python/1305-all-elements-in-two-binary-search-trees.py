from typing import List
from bintree_helper import TreeNode, deserialize, drawtree

'''
1. in-order traverse first tree
2. in-order traverse second tree
3. merge them
'''

def inorder(root):
    if root is None: return []
    if root.left is None and root.right is None: return [root.val]
    return inorder(root.left) + [root.val] + inorder(root.right)

def merge(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result + list1[i:] + list2[j:]

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = inorder(root1)
        list2 = inorder(root2)
        return merge(list1, list2)

root1 = "[2,1,4]"
root2 = "[1,0,3]"
result = Solution().getAllElements(deserialize(root1), deserialize(root2))
assert result == [0,1,1,2,3,4]

root1 = "[0,-10,10]"
root2 = "[5,1,7,0,2]"
result = Solution().getAllElements(deserialize(root1), deserialize(root2))
assert result == [-10,0,0,1,2,5,7,10]

root1 = "[null]"
root2 = "[5,1,7,0,2]"
result = Solution().getAllElements(deserialize(root1), deserialize(root2))
assert result == [0,1,2,5,7]

root1 = "[0,-10,10]"
root2 = "[null]"
result = Solution().getAllElements(deserialize(root1), deserialize(root2))
assert result == [-10,0,10]

root1 = "[1,null,8]"
root2 = "[8,1]"
result = Solution().getAllElements(deserialize(root1), deserialize(root2))
assert result == [1,1,8,8]