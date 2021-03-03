from typing import List, Optional

'''
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91059/Java-O(n)-solution-using-Trie

ex: 
nums = [14, 11, 7, 2], binary_form = [1110, 1011, 0111, 0010]
Trie:
                root
            .          .
          0              1
        .   .          .   .
       0     1        0     1
        .      .        .     .
         1      1        1     1
        .        .        .   .
       0          1        1 0
       2          7       11 14
'''

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        "Trie, Time: O(32n), Space: O(32n)"
        class TrieNode:
            def __init__(self):
                self.links: List[Optional["TrieNode"]] = [None, None]
        root = TrieNode()
        ans = float("-inf")
        # Build Trie
        for num in nums:
            cur = root
            for i in reversed(range(32)):
                bit = (num>>i) & 1 # The ith bit from right
                if cur.links[bit] is None: cur.links[bit] = TrieNode()
                cur = cur.links[bit]
        # For each num, Find the max with its complement
        ans = 0
        for num in nums:
            cur = root
            result = 0
            for i in reversed(range(32)):
                bit = (num>>i) & 1
                if cur.links[1-bit]: 
                    result += (1<<i)
                    cur = cur.links[1-bit]
                else: 
                    result += (0<<i)
                    cur = cur.links[bit]
            ans = max(ans, result)
        return ans
    def findMaximumXOR(self, nums: List[int]) -> int:
        "Improvement of above build trie and find at the same time, Time: above/2, Space: O(32n)"
        class TrieNode:
            def __init__(self):
                self.links: List[Optional["TrieNode"]] = [None, None]
        root = TrieNode()
        ans = 0
        for num in nums:
            cur, complement = root, root # cur for build trie, complement for find max
            result = 0
            for i in reversed(range(32)):
                bit = (num>>i) & 1 # The ith bit from right
                if cur.links[bit] is None: cur.links[bit] = TrieNode()
                if complement.links[1-bit]:
                    result += (1<<i)
                    complement = complement.links[1-bit]
                else:
                    result += (0<<i)
                    complement = complement.links[bit]
                cur = cur.links[bit]
            ans = max(ans, result)
        return ans

nums = [3,10,5,25,2,8]
ans = Solution().findMaximumXOR(nums)
assert ans == 28

nums = [0]
ans = Solution().findMaximumXOR(nums)
assert ans == 0

nums = [2,4]
ans = Solution().findMaximumXOR(nums)
assert ans == 6

nums = [8,10,2]
ans = Solution().findMaximumXOR(nums)
assert ans == 10

nums = [14,70,53,83,49,91,36,80,92,51,66,70]
ans = Solution().findMaximumXOR(nums)
assert ans == 127