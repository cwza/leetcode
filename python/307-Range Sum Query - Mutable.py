
from typing import List


class NumArray:
    "Binary Index Tree"
    "Can only be used on RangeSum"
    "https://www.youtube.com/watch?v=WbafSgetDDk&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=19"
    def __init__(self, nums: List[int]):
        "Time: O(nlogn)"
        self.nums = [0]*len(nums)
        self.tree = [0]*(len(nums)+1) # Note that tree[0] is not used, We start from 1
        for i, num in enumerate(nums):
            self.update(i, num)
    def update(self, i: int, val: int) -> None:
        "Time: O(logn)"
        def helper(x, delta):
            "increases the value at position x by delta, Note that this x is start from 1 not 0"
            while x < len(self.tree):
                self.tree[x] += delta
                x += x & -x
        helper(i+1, val-self.nums[i])
        self.nums[i] = val
    def sumRange(self, i: int, j: int) -> int:
        "Time: O(logn)"
        def helper(x):
            "return the sum from 1 to x, use 1_index"
            s = 0
            while x > 0:
                s += self.tree[x]
                x -= x & -x
            return s
        return helper(j+1) - helper(i+1-1) # get range_sum from prefix sum


class NumArray:
    "Segment Tree by TreeNode and Recursive"
    "Can be used on RangeSum, RangeMin, RangeMax, ...etc"
    "https://www.youtube.com/watch?v=rYBtViWXYeI&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=8"
    """
    Ex: nums = [5, 8, 6, 3, 2, 7, 2, 6]
        tree =
                      39
                   .     .
                 22       17
                .  .     .   .
              13    9   9     8  
             . .   . . . .   . .
            [5 8   6 3 2 7   2 6]
    """
    class SegmentTreeNode:
        def __init__(self, start, end, s, left=None, right=None):
            self.start = start
            self.end = end
            self.s = s
            self.left, self.right = left, right
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build_tree(nums)
    def build_tree(self, nums):
        "Time: O(n), Space: O(n)"
        def helper(start, end):
            if end < start: return None
            if start == end: return NumArray.SegmentTreeNode(start, end, nums[start])
            mid = start + (end-start)//2
            left = helper(start, mid)
            right = helper(mid+1, end)
            return NumArray.SegmentTreeNode(start, end, left.s+right.s, left, right) # If we need RangeMin, Change + to min
        return helper(0, len(nums)-1)
    def update(self, i: int, val: int) -> None:
        "Time: O(logn)"
        self.nums[i] = val
        def helper(root):
            if root.start == root.end == i:
                root.s = val
                return
            mid = root.start + (root.end-root.start)//2
            if i <= mid: helper(root.left)
            else: helper(root.right)
            root.s = root.left.s + root.right.s # If we need RangeMin, Change + to min
        helper(self.root)
    def sumRange(self, i: int, j: int) -> int:
        "Time: O(logn)"
        def helper(root, l, r):
            if root.start == l and root.end == r: return root.s
            mid = root.start + (root.end-root.start)//2
            if r <= mid: return helper(root.left, l, r)
            elif l > mid: return helper(root.right, l, r)
            return helper(root.left, l, mid) + helper(root.right, mid+1, r) # If we need RangeMin, Change + to min
        return helper(self.root, i, j)


class NumArray:
    "Segment Tree by Array and Iterative"
    "https://leetcode.com/problems/range-sum-query-mutable/solution/"
    """
    Ex: nums = [5, 8, 6, 3, 2, 7, 2, 6]
                0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
        tree = [0, 39, 22, 17, 13,  9,  9,  8,  5,  8,  6,  3,  2,  7,  2,  6]
                     39
                   .     .
                 22       17
                .  .     .   .
              13    9   9     8  
             . .   . . . .   . .
            [5 8   6 3 2 7   2 6]
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = self.build_tree(nums)
    def build_tree(self, nums):
        "Time: O(n), Space: O(n)"
        n = len(nums)
        tree = [0] * (2*n)
        for i in range(n):
            tree[i+n] = nums[i]
        for i in reversed(range(1, n)):
            tree[i] = tree[i*2] + tree[i*2+1] # If we need RangeMin, Change + to min
        return tree
    def update(self, i: int, val: int) -> None:
        "Time: O(logn)"
        self.nums[i] = val
        n = len(self.nums)
        i += n
        self.tree[i] = val
        while i > 0:
            l, r = i, i
            if i%2==0: r = i + 1
            else: l = i - 1
            self.tree[i//2] = self.tree[l] + self.tree[r] # If we need RangeMin, Change + to min
            i //= 2
    def sumRange(self, i: int, j: int) -> int:
        "Time: O(logn)"
        n = len(self.nums)
        l, r = i+n, j+n
        s = 0 # If we need RangeMin, Change init of s to +inf
        while l <= r:
            if l%2==1:
                s += self.tree[l] # If we need RangeMin, Change + to min
                l += 1
            if r%2==0:
                s += self.tree[r] # If we need RangeMin, Change + to min
                r -= 1
            l //= 2
            r //= 2
        return s

# nums = [1,3,4,8,6,1,4,2]
# solution = NumArray(nums)
# print(solution.tree)

# nums = [5, 8, 6, 3, 2, 7, 2, 6]
# solution = NumArray(nums)
# print(solution.tree)

nums = [1, 3, 5]
solution = NumArray(nums)
assert solution.sumRange(0, 2) == 9
solution.update(1, 2)
assert solution.sumRange(0, 2) == 8

nums = []
solution = NumArray(nums)