from collections import Counter

'''
How to check whether one string is a permutation of another string?
1. Sort the string and then compare
2. Both strings must have same character frequencies
https://leetcode.com/problems/permutation-in-string/solution/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        "Approach2: Sort, Time: O(l1logl1 + (l2-l1)*(l1logl1+l1)), Space: O(1), TLE"
        s1 = sorted(s1) # O(l1logl1)
        window_sz = len(s1)
        for i in range(len(s2)-window_sz+1): # O(l2-l1)
            sub_s2 = sorted(s2[i:i+window_sz]) # O(l1logl1)
            if s1 == sub_s2: return True # O(l1)
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        "Approach3: HashTable, Time: O(l1+(l2-l1)*l1), Space: O(1)"
        counter1 = Counter(s1) # O(l1)
        window_sz = len(s1)
        for i in range(len(s2)-window_sz+1): # O(l2-l1)
            counter2 = Counter(s2[i:i+window_sz])  # O(l1)
            if counter1 == counter2: return True # O(26)
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        "Approach5 but use Counter: HashTable + Sliding Window, Time: O(l1+(l2-l1)), Space: O(1)"
        counter1 = Counter(s1) # O(l1)
        window_sz = len(s1)

        counter2 = Counter(s2[:window_sz])
        if counter1 == counter2: return True
        for i in range(1, len(s2)-window_sz+1): # O(l2-l1)
            counter2[s2[i-1]] -= 1
            if counter2[s2[i-1]] <= 0: del counter2[s2[i-1]]
            counter2[s2[i+window_sz-1]] += 1
            if counter1 == counter2: return True # O(26)
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        "Approach5: Array + Sliding Window, Time: O(l1+(l2-l1)), Space: O(1)"
        if len(s1) > len(s2): return False
        window_sz = len(s1)
        counter1, counter2 = [0]*26, [0]*26
        for i in range(window_sz): # O(l1)
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1
        if counter1 == counter2: return True
        for i in range(1, len(s2)-window_sz+1): # O(l2-l1)
            counter2[ord(s2[i-1]) - ord('a')] -= 1
            counter2[ord(s2[i+window_sz-1]) - ord('a')] += 1
            if counter1 == counter2: return True # O(26)
        return False

s1 = "ab"
s2 = "eidbaooo"
result = Solution().checkInclusion(s1, s2)
assert result == True

s1= "ab"
s2 = "eidboaoo"
result = Solution().checkInclusion(s1, s2)
assert result == False