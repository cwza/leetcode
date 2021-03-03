from typing import List

'''
Tricky part is block_state, its index is row//3*3+col//3
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        "Backtracking, Time: 9^(81)"
        """
        Do not return anything, modify board in-place instead.
        """
        row_state = [[True]*10 for _ in range(9)]
        col_state = [[True]*10 for _ in range(9)]
        block_state = [[True]*10 for _ in range(9)]
        def available_nums(row, col):
            for num in range(1, 10):
                if row_state[row][num] and col_state[col][num] and block_state[row//3*3+col//3][num]:
                    yield num
        def dfs(level):
            if level == 81: return False
            row, col = divmod(level, 9)
            if board[row][col] != '.': 
                return dfs(level+1)
            else:
                for num in available_nums(row, col):
                    board[row][col] = str(num)
                    row_state[row][num] = False
                    col_state[col][num] = False
                    block_state[row//3*3+col//3][num] = False
                    if dfs(level+1) == False: return False
                    board[row][col] = "."
                    row_state[row][num] = True
                    col_state[col][num] = True
                    block_state[row//3*3+col//3][num] = True
                return True
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    row_state[row][num] = False
                    col_state[col][num] = False
                    block_state[row//3*3+col//3][num] = False
        dfs(0)
    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]