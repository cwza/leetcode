from bintree_helper import *

class Solution:
    def isSameTree(self, p, q) -> bool:
        "DFS, Time: O(n), Space: O(n)"
        def dfs(l, r):
            if l is None and r is None: return True
            if l is None or r is None: return False
            return l.val == r.val and dfs(l.left, r.left) and dfs(l.right, r.right)
        return dfs(p, q)
    def isSameTree(self, p, q) -> bool:
        "BFS, Time: O(n), Space: O(n)"
        from collections import deque
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            l = q1.popleft()
            r = q2.popleft()
            if l is None and r is None: continue
            if l is None or r is None: return False
            if l.val != r.val: return False
            q1.append(l.left)
            q1.append(l.right)
            q2.append(r.left)
            q2.append(r.right)
        if len(q1) == 0 and len(q2) == 0: return True
        return False

p = deserialize("[1,2,3]")
q = deserialize("[1,2,3]")
result = Solution().isSameTree(p, q)
assert result == True

p = deserialize("[1,2]")
q = deserialize("[1,null,2]")
result = Solution().isSameTree(p, q)
assert result == False

p = deserialize("[1,2,1]")
q = deserialize("[1,1,2]")
result = Solution().isSameTree(p, q)
assert result == False