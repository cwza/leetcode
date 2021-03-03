from typing import List
from itertools import permutations

'''
Brute Force will result in TLE because n >> k (n: length of words, k: avg length of word)
O(n*k^2) is tricky, please see:
https://www.youtube.com/watch?v=XpxCzLl61lU
https://medium.com/@bill800227/leetcode-336-palindrome-pairs-875f9e52c99d
'''

def is_palindrome(word):
    i, j = 0, len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

class Solution:
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     "Brute Force, Time: O(n^2*k), Space: O(1)"
    #     "Generate all pairs and check all of them, result TLE"
    #     perms = permutations(zip(words, range(len(words))), 2)
    #     result = []
    #     for left, right in perms:
    #         left_word, left_idx = left
    #         right_word, right_idx = right
    #         if is_palindrome(left_word+right_word):
    #             result.append([left_idx, right_idx])
    #     return result
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        "HashMap, Time: O(n*k^2), Space: O(n)"
        reverse_dict = {word[::-1]: idx for idx, word in enumerate(words)} # reversed word: idx
        result = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                mid = word[:j]
                right = word[j:]
                if is_palindrome(mid) and right in reverse_dict:
                    left_idx = reverse_dict[right]
                    if left_idx != i:
                        result.append((left_idx, i))
            for j in range(len(word)-1, -1, -1):
                mid = word[j:]
                left = word[:j]
                if is_palindrome(mid) and left in reverse_dict:
                    right_idx = reverse_dict[left]
                    if right_idx != i:
                        result.append((i, right_idx))
        return result

words = ["abcd","dcba","lls","s","sssll"]
result = Solution().palindromePairs(words)
print(result) # [[0,1],[1,0],[3,2],[2,4]]

words = ["bat","tab","cat"]
result = Solution().palindromePairs(words)
print(result) # [[0,1],[1,0]]

words = ["a",""]
result = Solution().palindromePairs(words)
print(result) # [[0,1],[1,0]]