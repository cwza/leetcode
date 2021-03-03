from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        tmp = t - 3000
        while self.queue[0] < tmp:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

obj = RecentCounter()
requests = [1, 100, 3001, 3002]
result = [obj.ping(request) for request in requests]
print(result)
assert result == [1, 2, 3, 3]