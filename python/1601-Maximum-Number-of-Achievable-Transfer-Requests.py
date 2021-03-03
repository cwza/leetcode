from typing import List

'''
Brute Force try all combinations of requests
'''

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        "O(2^n), n is len(request), n is <=16"
        result = [0]
        balance = [0] * n
        def helper(depth, count):
            if depth == len(requests):
                if any(balance) == False:
                    result[0] = max(result[0], count)
                return
            
            helper(depth+1, count)

            ori, dest = requests[depth]
            balance[ori] -= 1
            balance[dest] += 1
            helper(depth+1, count+1)
            balance[ori] += 1
            balance[dest] -= 1
        helper(0, 0)
        return result[0]

n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
result = Solution().maximumRequests(n, requests)
assert result == 5

n = 3
requests = [[0,0],[1,2],[2,1]]
result = Solution().maximumRequests(n, requests)
assert result == 3

n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
result = Solution().maximumRequests(n, requests)
assert result == 4