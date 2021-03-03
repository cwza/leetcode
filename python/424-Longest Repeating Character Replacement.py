from collections import Counter

'''
https://www.cnblogs.com/grandyang/p/5999050.html
我们首先来想，如果没有k的限制，
让我们求把字符串变成只有一个字符重复的字符串需要的最小置换次数，
那么就是字符串的总长度减去出现次数最多的字符的个数。
如果加上k的限制，我们其实就是求满足 (子字符串的长度减去出现次数最多的字符个数)<=k 的最大子字符串长度即可
cur_window_len - most_freq <= k
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        "Sliding Window, Time: O(n), Space: O(1)"
        n = len(s)
        counter = Counter()
        l, result = 0, 0
        for r in range(n): # O(n)
            counter[s[r]] += 1
            most_freq = counter.most_common(1)[0][1] # O(26)
            while (r-l+1)-most_freq > k: # cur_window_len = r-l+1
                counter[s[l]] -= 1
                if counter[s[l]] == 0: del counter[s[l]]
                l += 1
            result = max(result, r-l+1)
        return result

s = "ABAB"
k = 2
result = Solution().characterReplacement(s, k)
assert result == 4

s = "AABABBA"
k = 1
result = Solution().characterReplacement(s, k)
assert result == 4