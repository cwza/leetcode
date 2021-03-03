from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        "HashMap + Custom sort, Time: O(nlogn), Space: O(n)"
        counter = Counter(s) # O(n)
        result = sorted(s, key=lambda x: (-counter[x], x)) # O(nlogn)
        return "".join(result) # O(n)
    def frequencySort(self, s: str) -> str:
        "HashMap + Heap, Time: O(n), Space: O(n)"
        import heapq
        from collections import defaultdict
        counter = defaultdict(lambda: 0)
        for ch in s: # O(n)
            counter[ch] += 1
        max_heap = []
        for ch, count in counter.items(): # O(26)
            heapq.heappush(max_heap, (-count, ch)) # O(log26)
        result = []
        while max_heap: # O(26)
            minus_count, ch = heapq.heappop(max_heap) # O(log26)
            count = -minus_count
            result.append(ch*count)
        return "".join(result) # O(n)
    def frequencySort(self, s: str) -> str:
        "Counter + most_common, Time: O(n), Space: O(n)"
        result = [ch*count for ch, count in Counter(s).most_common()] # O(n + 26*log26)
        return "".join(result)
s = "tree"
result = Solution().frequencySort(s)
print(result) # "eert"

s = "cccaaa"
result = Solution().frequencySort(s)
print(result) # "cccaaa"

s = "Aabb"
result = Solution().frequencySort(s)
print(result) # "bbAa"

s = "loveleetcode"
result = Solution().frequencySort(s)
print(result) # "eeeeoollvtdc"