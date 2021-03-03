from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log =="./":
                continue
            elif log == "../":
                if result == 0:
                    continue
                else:
                    result -= 1
            else:
                result += 1
        return result

logs = ["d1/","d2/","../","d21/","./"]
result = Solution().minOperations(logs)
assert result == 2

logs = ["d1/","d2/","./","d3/","../","d31/"]
result = Solution().minOperations(logs)
assert result == 3

logs = ["d1/","../","../","../"]
result = Solution().minOperations(logs)
assert result == 0
