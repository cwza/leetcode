from typing import List

class Solution:
    # def longestWord(self, words: List[str]) -> str:
    #     "HashSet, Time: O(n*m^2), Space: O(n), n=len(words), m=avg len of word"
    #     table = set(words)
    #     result = ""
    #     for word in words:
    #         if (len(word)>len(result)) or (len(word)==len(result) and word<result):
    #             if all([word[0:j] in table for j in range(1, len(word))]):
    #                 result = word
    #     return result
    def longestWord(self, words: List[str]) -> str:
        "Trie, Time: O(nm), Space: O(nm), n=len(words), m=avg len of word"
        class TrieNode:
            def __init__(self):
                self.links = {}
                self.is_end = False
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            def insert(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.links:
                        node.links[ch] = TrieNode()
                    node = node.links[ch]
                node.is_end = True
            def is_ok(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.links or node.links[ch].is_end == False:
                        return False
                    node = node.links[ch]
                return True
        # Build trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)
        # Search
        result = ""
        for word in words:
            if (len(word)>len(result)) or (len(word)==len(result) and word<result):
                if trie.is_ok(word):
                    result = word
        return result
words = ["w","wo","wor","worl", "world"]
result = Solution().longestWord(words)
assert result == "world"

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
result = Solution().longestWord(words)
assert result == "apple"