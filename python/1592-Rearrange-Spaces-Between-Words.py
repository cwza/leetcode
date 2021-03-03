


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num_words = len(words)
        num_spaces = sum([1 for ch in text if ch == ' '])

        if num_words == 1:
            return words[0]+' '*num_spaces

        num_between = num_spaces // (num_words-1)
        num_remain = num_spaces % (num_words-1)
        result = ''
        for i in range(num_words-1):
            result += words[i]+' '*num_between
        result += words[-1]+' '*num_remain
        return result

text = "  this   is  a sentence "
result = Solution().reorderSpaces(text)
assert result == "this   is   a   sentence"

text = " practice   makes   perfect"
result = Solution().reorderSpaces(text)
assert result == "practice   makes   perfect "

text = "hello   world"
result = Solution().reorderSpaces(text)
assert result == "hello   world"

text = "  walks  udp package   into  bar a"
result = Solution().reorderSpaces(text)
assert result == "walks  udp  package  into  bar  a "

text = "a"
result = Solution().reorderSpaces(text)
assert result == "a"