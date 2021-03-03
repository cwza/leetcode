from collections import deque

'''
https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O(n)-greedy-with-stack-explained
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        "Greedy, Time: O(n), Space: O(n)"
        last_occur = {ch:i for i, ch in enumerate(s)}
        visited = set()
        stack = deque('!')
        for i, ch in enumerate(s):
            if ch in visited: continue
            while ch < stack[-1] and last_occur[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)[1:]

s = "bcabc"
result = Solution().removeDuplicateLetters(s)
assert result == "abc"

s = "cbacdcbc"
result = Solution().removeDuplicateLetters(s)
assert result == "acdb"