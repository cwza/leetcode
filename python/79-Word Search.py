from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        "Backtracking"
        m = len(board)
        n = len(board[0])
        visited = set()
        def get_next_poses(x, y):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in dirs:
                next_x, next_y = x + dir[0], y + dir[1]
                if 0<=next_x<m and 0<=next_y<n and (next_x, next_y) not in visited:
                    yield next_x, next_y
        def dfs(i, x, y):
            if board[x][y] != word[i]: return False
            if i == len(word)-1: return True
            visited.add((x, y))
            for next_x, next_y in get_next_poses(x, y):
                if dfs(i+1, next_x, next_y): return True
            visited.remove((x, y))
            return False
        for x in range(m):
            for y in range(n):
                if dfs(0, x, y): return True
        return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
result = Solution().exist(board, word)
assert result == True

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"
result = Solution().exist(board, word)
assert result == True

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
result = Solution().exist(board, word)
assert result == False

board = [["a","b"],
         ["c","d"]]
word = "acdb"
result = Solution().exist(board, word)
assert result == True