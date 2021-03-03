from typing import List

'''
http://zxi.mytechroad.com/blog/searching/leetcode-51-n-queens/
Tricky part is the diag1_state and diag2_state, see picture of above url to understand why diag1_state[row+col], diag2_state[row-col+(n-1)]
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        "Backtracking, Time: O(n!)"
        col_state = [True]*n
        diag1_state = [True]*(2*n-1)
        diag2_state = [True]*(2*n-1)

        def available_cols(row):
            for col in range(n):
                if col_state[col] and diag1_state[row+col] and diag2_state[row-col+(n-1)]:
                    yield col

        cols = [-1]*n
        ans = []
        def dfs(row):
            if row == n:
                ans.append(['.'*cols[row]+'Q'+'.'*(n-cols[row]-1) for row in range(n)])
                return
            for col in available_cols(row):
                col_state[col] = False
                diag1_state[row+col] = False
                diag2_state[row-col+(n-1)] = False
                cols[row] = col
                dfs(row+1)
                col_state[col] = True
                diag1_state[row+col] = True
                diag2_state[row-col+(n-1)] = True
                cols[row] = -1
        dfs(0)
        return ans

n = 4
ans = Solution().solveNQueens(n)
assert ans == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

n = 1
ans = Solution().solveNQueens(n)
assert ans == [["Q"]]