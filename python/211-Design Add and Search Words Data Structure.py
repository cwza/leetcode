
"Trie + DFS"

class WordDictionary:
    class TrieNode():
        def __init__(self):
            self.is_end = False
            self.links = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch] = self.TrieNode()
            node = node.links[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(root, word):
            node = root
            for i, ch in enumerate(word):
                if ch == '.':
                    for child in node.links.values():
                        r = helper(child, word[i+1:])
                        if r:
                            return True
                    return False
                else:
                    if ch not in node.links:
                        return False
                    node = node.links[ch]
            return node.is_end
        return helper(self.root, word)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True