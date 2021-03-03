from functools import lru_cache
'''
DP:
dp(i, j): True if s[i:j+1] is palindrome else False
dp(i, j) = dp(i+1, j-1) and s[i] == s[j]
dp(i, i) = 1
dp(i, i+1) = s[i] == s[i+1]
'''

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     "Brute force, Time: O(n^3), Space: O(1), TLE"
    #     n = len(s)
    #     result_len = 0
    #     result = ""
    #     for i in range(n):
    #         for j in range(i, n):
    #             if j-i+1 <= result_len:
    #                 continue
    #             if s[i:j+1] == s[i:j+1][::-1]:
    #                 result_len = j - i + 1
    #                 result = s[i:j+1]
    #     return result
    # def longestPalindrome(self, s: str) -> str:
    #     "Top-Down + Memoization, Time: O(n^2), Space: O(n^2), TLE"
    #     @lru_cache(None)
    #     def is_palindrone(i, j):
    #         if j <= i: return True
    #         return s[i] == s[j] and is_palindrone(i+1, j-1) 
    #     n = len(s)
    #     result_len = 0
    #     result = ""
    #     for i in range(n):
    #         for j in range(i, n):
    #             if j-i+1 <= result_len:
    #                 continue
    #             if is_palindrone(i, j):
    #                 result_len = j-i+1
    #                 result = s[i:j+1]
    #     return result 
    # def longestPalindrome(self, s: str) -> str:
    #     "Down-Top DP, Time: O(n^2), Space: O(n^2), TLE"
    #     n = len(s)
    #     dp = [[False for j in range(n)] for i in range(n)]
    #     result_len = 0
    #     result = ""
    #     for j in range(n):
    #         for i in range(j+1):
    #             if i == j: dp[i][j] = True
    #             elif j == i + 1: dp[i][j] = s[i] == s[j]
    #             else: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
    #             if j-i+1 <= result_len:
    #                 continue
    #             if dp[i][j]:
    #                 result_len = j - i + 1
    #                 result = s[i:j+1]
    #     return result              
    def longestPalindrome(self, s: str) -> str:
        '''
        https://www.youtube.com/watch?v=XYQecbcd6_c
        Expand Around Center, Time: O(n^2), Space: O(1)
        '''
        n = len(s)
        result_len = 0
        result = ""
        for i in range(n):
            # Odd Case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result_len = r - l + 1
                    result = s[l:r+1]
                l -= 1
                r += 1
            # Even Case
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result_len = r - l + 1
                    result = s[l:r+1]
                l -= 1
                r += 1
        return result

s = "babad"
result = Solution().longestPalindrome(s)
print(result) # "bab" or "aba"

s = "cbbd"
result = Solution().longestPalindrome(s)
print(result) # "bb"

s = "a"
result = Solution().longestPalindrome(s)
print(result) # "a"

s = "ac"
result = Solution().longestPalindrome(s)
print(result) # "a"

s = "vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"
result = Solution().longestPalindrome(s)
print(result) # "oxaxo"
