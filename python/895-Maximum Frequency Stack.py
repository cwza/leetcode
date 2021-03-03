from collections import Counter, defaultdict, deque
from heapq import heappush, heappop

# class FreqStack:
#     "Frequency HashMap + Priority Queue"
#     def __init__(self):
#         "Space: O(n)"
#         self.freq_map = Counter()
#         self.pq = [] # (-freq, -idx, value)
#         self.idx = 0
#     def push(self, x: int) -> None:
#         "Time: O(logn)"
#         self.freq_map[x] += 1
#         freq = self.freq_map[x]
#         heappush(self.pq, (-freq, -self.idx, x))
#         self.idx += 1
#     def pop(self) -> int:
#         "Time: O(logn)"
#         _, _, x = heappop(self.pq)
#         self.freq_map[x] -= 1
#         return x

class FreqStack:
    "Value to Frequency HashMap + Frequency to Values HashMap"
    def __init__(self):
        "Space: O(n)"
        self.val_freq_map = Counter()
        self.freq_vals_map = defaultdict(deque)
        self.max_freq = 0
    def push(self, x: int) -> None:
        "Time: O(1)"
        self.val_freq_map[x] += 1
        freq = self.val_freq_map[x]
        self.max_freq = max(self.max_freq, freq)
        values = self.freq_vals_map[freq]
        values.append(x)
    def pop(self) -> int:
        "Time: O(1)"
        values = self.freq_vals_map[self.max_freq]
        x = values.pop()
        self.val_freq_map[x] -= 1
        if len(values) == 0:
            self.max_freq -= 1
        return x

freq_stack = FreqStack()
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(4)
freq_stack.push(5)
assert freq_stack.pop() == 5
assert freq_stack.pop() == 7
assert freq_stack.pop() == 5
assert freq_stack.pop() == 4
assert freq_stack.pop() == 7
assert freq_stack.pop() == 5

freq_stack = FreqStack()
freq_stack.push(4)
freq_stack.push(0)
freq_stack.push(9)
freq_stack.push(3)
freq_stack.push(4)
freq_stack.push(2)
assert freq_stack.pop() == 4
freq_stack.push(6)
assert freq_stack.pop() == 6
freq_stack.push(1)
assert freq_stack.pop() == 1
freq_stack.push(1)
assert freq_stack.pop() == 1
freq_stack.push(4)
assert freq_stack.pop() == 4
assert freq_stack.pop() == 2
assert freq_stack.pop() == 3
assert freq_stack.pop() == 9
assert freq_stack.pop() == 0
assert freq_stack.pop() == 4

