from typing import List
from collections import defaultdict, deque

'''
Sliding Window
'''

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        "O(nlogn)"
        def get_time(str_time):
            hour, minute = str_time.split(':')[0], str_time.split(':')[1]
            return int(hour) * 60 + int(minute)
        def preprocess(keyName, keyTime):
            table = defaultdict(list)
            for name, str_time in zip(keyName, keyTime):
                table[name].append(get_time(str_time))
            return table
        def is_alert(times):
            times.sort()
            window = deque()
            for time in times:
                while window and window[0] < time - 60:
                    window.popleft()
                window.append(time)
                if len(window) >= 3:
                    return True
            return False
        results = []
        table = preprocess(keyName, keyTime)
        for name, times in table.items():
            if is_alert(times):
                results.append(name)
        return sorted(results)

keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
result = Solution().alertNames(keyName, keyTime)
assert result == ["daniel"]

keyName = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
result = Solution().alertNames(keyName, keyTime)
assert result == ["bob"]

keyName = ["john","john","john"]
keyTime = ["23:58","23:59","00:01"]
result = Solution().alertNames(keyName, keyTime)
assert result == []

keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
result = Solution().alertNames(keyName, keyTime)
assert result == ["clare", "leslie"]