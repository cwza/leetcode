from collections import Counter
import heapq

'''
https://www.cnblogs.com/grandyang/p/8799483.html
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        "Greedy + Heap, Time: O(n), Space: O(n)"
        n = len(S)
        counter = Counter(S) # O(n)
        max_heap = [(-count, ch) for ch, count in counter.most_common()] # O(26+26log26)
        heapq.heapify(max_heap)
        if -max_heap[0][0] > (n+1)//2:
            return ""
        result = []
        while len(max_heap) > 1: # O(n)
            minus_count1, ch1 = heapq.heappop(max_heap)
            minus_count2, ch2 = heapq.heappop(max_heap)
            count1, count2 = -minus_count1, -minus_count2
            result.extend([ch1, ch2])
            if count1-1 > 0: heapq.heappush(max_heap, (-(count1-1), ch1))
            if count2-1 > 0: heapq.heappush(max_heap, (-(count2-1), ch2))
        if max_heap:
            _, ch = heapq.heappop(max_heap)
            result.append(ch)
        return "".join(result)

S = "aab"
result = Solution().reorganizeString(S)
print(result) # "aba"

S = "aaab"
result = Solution().reorganizeString(S)
assert result == ""