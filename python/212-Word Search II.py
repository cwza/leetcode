from typing import List

class Trie:
    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.links = {}
    def __init__(self):
        self.root = self.TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch] = self.TrieNode()
            node = node.links[ch]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        "Trie + Backtracking"
        "https://www.youtube.com/watch?v=fxnFcriLzvY"
        # Build trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie_root = trie.root

        # Run Backtracking
        m = len(board)
        n = len(board[0])
        done = set()
        def next_candidates(cur, done):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            result = []
            for dir in dirs:
                new = (cur[0]+dir[0], cur[1]+dir[1])
                if 0 <= new[0] < m and 0 <= new[1] < n and new not in done:
                    result.append(new)
            return result
        result = set()
        def back_track(path, candidates, trie_node):
            if trie_node.is_end:
                result.add(path)
            for candidate in candidates:
                x, y = candidate[0], candidate[1]
                ch = board[x][y]
                if ch in trie_node.links:
                    done.add((x, y))
                    back_track(path+ch, next_candidates((x, y), done), trie_node.links[ch])
                    done.remove((x, y))
        back_track("", [[i, j] for i in range(m) for j in range(n)], trie_root)
        return result

board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
result = Solution().findWords(board, words)
print(result) # ["eat","oath"]

board = [["a","b"],
         ["c","d"]]
words = ["abcb"]
result = Solution().findWords(board, words)
print(result) # []

board = [["a","a"]]
words = ["a"]
result = Solution().findWords(board, words)
print(result) # ["a"]