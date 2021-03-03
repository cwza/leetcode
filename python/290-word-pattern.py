class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words): return False
        table1 = {}
        table2 = {}
        for i in range(len(pattern)):
            word = words[i]
            p = pattern[i]
            if p in table1:
                if table1[p] != word:
                    return False
            if word in table2:
                if table2[word] != p:
                    return False
            table1[p] = word
            table2[word] = p
        return True

pattern = "abba"
str = "dog cat cat dog"
result = Solution().wordPattern(pattern, str)
assert result == True

pattern = "abba"
str = "dog cat cat fish"
result = Solution().wordPattern(pattern, str)
assert result == False

pattern = "aaaa"
str = "dog cat cat dog"
result = Solution().wordPattern(pattern, str)
assert result == False

pattern = "abba"
str = "dog dog dog dog"
result = Solution().wordPattern(pattern, str)
assert result == False