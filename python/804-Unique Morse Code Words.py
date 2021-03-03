from typing import List

def get_morse_code(ch):
    mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return mapping[ord(ch) - ord("a")]

def get_concatenation(word):
    concatenation = ""
    for ch in word:
        concatenation += get_morse_code(ch)
    return concatenation

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        "Time: O(nm), Space: O(n), len(words): n, avg len(word): m"
        concatenations = set([get_concatenation(word) for word in words])
        return len(concatenations)

words = ["gin", "zen", "gig", "msg"]
result = Solution().uniqueMorseRepresentations(words)
assert result == 2
