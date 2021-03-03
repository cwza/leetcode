from typing import List

# class WordFilter:
#     '''
#     Approch1: 2 Tries
#     Algorithm:
#     1. Construct 2 tries, one for prefix, one for suffix
#         TrieNode should store the word_idxs for this prefix
#     2. While search, get the word_idxs for prefix and suffix, take their intersection and returns the max one

#     Complexity: This approach will get TLE
#         N is the number of words, K is the maximum length of a word, and Q is the number of queries
#         Time: O(NK + Q(N+K))
#         Space: O(NK)
#     '''
#     class TrieNode:
#         def __init__(self, idx=None):
#             self.links = {}
#             self.idxs = set([idx]) if idx is not None else set()

#     def __init__(self, words: List[str]):
#         self.trie1_root = self.TrieNode() # For prefix
#         self.trie2_root = self.TrieNode() # For suffix, which stored the reversed words
#         def add_word(trie_root, word, word_idx):
#             node = trie_root
#             for ch in word:
#                 if ch not in node.links:
#                     node.links[ch] = self.TrieNode(word_idx)
#                 else:
#                     node.links[ch].idxs.add(word_idx)
#                 node = node.links[ch]
#         # Build 2 tries
#         for idx, word in enumerate(words):
#             add_word(self.trie1_root, word, idx)
#             add_word(self.trie2_root, word[::-1], idx)

#     def f(self, prefix: str, suffix: str) -> int:
#         node1 = self.trie1_root
#         for ch in prefix:
#             if ch in node1.links:
#                 node1 = node1.links[ch]
#         idxs_for_prefix = node1.idxs

#         node2 = self.trie2_root
#         for ch in suffix[::-1]:
#             if ch in node2.links:
#                 node2 = node2.links[ch]
#         idxs_for_suffix = node2.idxs

#         result_idxs = idxs_for_prefix.intersection(idxs_for_suffix)
#         return -1 if len(result_idxs) == 0 else max(result_idxs)

class WordFilter:
    '''
    Approach2: Hashmap
    Algorithm:
        1. Generate all possible prefix#suffix for all words
            ex: apple: a#e, a#le, a#ple, a#pple, a#apple, ap#e, ap#le, ....
        2. Use hashmap to store the mapping from prefix#suffix to max idx
        3. Construct the query string and search within hashmap
    Complexity:
        N is the number of words, K is the maximum length of a word, and Q is the number of queries
        Time: O(N*K^2 + Q), Space: O(N*K^2)
    '''
    def __init__(self, words: List[str]):
        self.mapping = {}
        for idx, word in enumerate(words):
            k = len(word)
            # Generate all prefix#suffix for word
            for i in range(1, k+1):
                prefix = word[:i]
                for j in range(k-1, -1, -1):
                    suffix = word[j:]
                    self.mapping[f'{prefix}#{suffix}'] = idx # if 2 words have the same prefix#suffix then the one with larger idx wins, so we can simply replace with later idx

    def f(self, prefix: str, suffix: str) -> int:
        query_str = f'{prefix}#{suffix}'
        return self.mapping[query_str] if query_str in self.mapping else -1

# class WordFilter:
#     '''
#     Approach3: 1 Trie, Tricky
#     Algorithm:
#         1. Ex: for apple, add following into trie '#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple'
#         2. search by suffix#prefix
#     Complexity:
#         N is the number of words, K is the maximum length of a word, and Q is the number of queries
#         Time: O(N*K^2 + QK), Space: O(N*K^2)
#     '''
#     class Trie:
#         class TrieNode:
#             def __init__(self, idx=-1):
#                 self.links = {}
#                 self.idx = idx # Same as above we can store one idx because the later idx is always larger
#         def __init__(self):
#             self.root = self.TrieNode()
#         def add_word(self, word, word_idx):
#             node = self.root
#             for ch in word:
#                 if ch not in node.links:
#                     node.links[ch] = self.TrieNode(word_idx)
#                 node = node.links[ch]
#                 node.idx = word_idx
#         def search(self, word) -> int:
#             node = self.root
#             for ch in word:
#                 if ch in node.links:
#                     node = node.links[ch]
#                 else:
#                     return -1
#             return node.idx
#     def __init__(self, words: List[str]):
#         self.trie = self.Trie()
#         for idx, word in enumerate(words):
#             k = len(word)
#             for i in range(k, -1, -1):
#                 suffix = word[i:]
#                 self.trie.add_word(f'{suffix}#{word}', idx)
#     def f(self, prefix: str, suffix: str) -> int:
#         query_str = f'{suffix}#{prefix}'
#         idx = self.trie.search(query_str)
#         return idx

wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e")) # return 0, because the word at index 0 has prefix = "a" and suffix = 'e".