from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        "Sequential Search: O(n), Space: O(1)"
        for letter in letters:
            if letter > target: return letter
        return letters[0]
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        "Binary Search: O(logn), Space: O(1)"
        l, r = 0, len(letters)
        while l < r:
            m = l + (r-l)//2
            if letters[m] > target: r = m
            else: l = m + 1
        if l == len(letters): return letters[0]
        return letters[l]

letters = ["c", "f", "j"]
target = "a"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'c'

letters = ["c", "f", "j"]
target = "c"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'f'

letters = ["c", "f", "j"]
target = "d"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'f'

letters = ["c", "f", "j"]
target = "g"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'j'

letters = ["c", "f", "j"]
target = "j"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'c'

letters = ["c", "f", "j"]
target = "k"
result = Solution().nextGreatestLetter(letters, target)
assert result == 'c'
