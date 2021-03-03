from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        "Use LeetCode 139, just call it on each word, be careful that the words may contains empty string which is not handled by LeetCode 139"
        "Time: O(n*(m^2)), Space: O(n+m), n: len(words), m: avg len(word)"
        
        def wordBreak(s, word_dict):
            if s == "": return False
            n = len(s)
            dp = [False] * (n+1)
            dp[0] = True

            for i in range(1, n+1):
                for j in range(i):
                    if s[j:i] in word_dict and dp[j]:
                        dp[i] = True
                        break
            
            return dp[-1]
        word_dict = set(words)
        result = []
        for word in words:
            word_dict.remove(word)
            if wordBreak(word, word_dict):
                result.append(word)
            word_dict.add(word)
        return result

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
result = Solution().findAllConcatenatedWordsInADict(words)
assert result == ["catsdogcats","dogcatsdog","ratcatdogcat"]