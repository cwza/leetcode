from collections import Counter

'''
O(n) Sliding window solution is very tricky.
https://www.youtube.com/watch?v=izjPlJrZ_K0

Key:
we will use sliding window approach to find the window of biggest length. However, it is not that easy. 
Imagine, that we have s = aabbb... and k = 3, what should we do when we reached window aabbb: should we expand it to the right hoping that we will meet another a? Or should we start to move left side of our window? 
One way to handle this problem is to do several sliding windows passes, where we fix T number of different symbols we must have in our substring. So, we check all posible T = 1, ... 26 (if fact, not 26, but len(Counter(s)) + 1)) and do sliding window pass
'''

class Solution:
    # def longestSubstring(self, s: str, k: int) -> int:
    #     "Brute Force, Time: O(26*n^2), Space: O(26), TLE"
    #     n = len(s)
    #     result = 0
    #     for i in range(n):
    #         counter = Counter()
    #         for j in range(i, n):
    #             ch = s[j]
    #             counter[ch] += 1
    #             if all([1 if count >= k else 0 for _, count in counter.items()]): # O(26)
    #                 result = max(result, j-i+1)
    #     return result
    # def longestSubstring(self, s: str, k: int) -> int:
    #     "Little improvement of above, Time: O(n^2), Space: O(26), TLE"
    #     n = len(s)
    #     result = 0
    #     for i in range(n):
    #         counter = Counter()
    #         # 001 if freq of a is not above k, but b, c above
    #         # 011 if freq of a, b is not above k, but c above
    #         # 000 if freq of a,b,c all above k
    #         mask = 0 
    #         for j in range(i, n):
    #             ch = s[j]
    #             counter[ch] += 1
    #             if counter[ch] < k:
    #                 mask |= 1 << (ord(ch) - ord('a'))
    #             else:
    #                 mask &= ~ (1 << (ord(ch) - ord('a')))
    #             if mask == 0:
    #                 result = max(result, j-i+1)
    #     return result
    # def longestSubstring(self, s: str, k: int) -> int:
    #     "Divide and Conquer, Time: Worst: O(n^2) Best: O(nlogn), Space: O(n)"
    #     def helper(i, j):
    #         if i == j:
    #             return 0
    #         counter = Counter(s[i:j])
    #         mids = [ch for ch, count in counter.items() if count < k]
    #         if len(mids) == 0:
    #             return j - i
    #         mid = s[i:j].index(mids[0]) + i
    #         return max(helper(i, mid), helper(mid+1, j))
    #     return helper(0, len(s))
    def longestSubstring(self, s: str, k: int) -> int:
        "Sliding Window, Time: O(26*n), Space: O(26)"
        counter = Counter(s)
        max_unique = len(counter)
        result = 0
        for max_window_size in range(1, max_unique+1):
            counter = Counter()
            i, j = 0, 0
            found = 0
            # len(counter) == number of current unique
            while j < len(s):
                counter[s[j]] += 1
                if len(counter) <= max_window_size:
                    if counter[s[j]] == k:
                        found += 1
                else:
                    while len(counter) > max_window_size:
                        counter[s[i]] -= 1
                        if counter[s[i]] == k-1:
                            found -= 1
                        if counter[s[i]] == 0:
                            del counter[s[i]]
                        i += 1
                if found == len(counter):
                    result = max(result, j-i+1)
                j += 1
        return result
s = "aaabb"
k = 3
result = Solution().longestSubstring(s, k)
assert result == 3

s = "ababbc"
k = 2
result = Solution().longestSubstring(s, k)
assert result == 5

