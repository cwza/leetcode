from typing import List
import copy
from collections import deque

'''
Backtracking
'''

def init(grid):
    done_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                start_pos = (i, j)
                done_grid[i][j] = 0
            elif grid[i][j] == 2:
                end_pos = (i, j)
                done_grid[i][j] = 0
            elif grid[i][j] == -1:
                done_grid[i][j] = 1
            else:
                done_grid[i][j] = 0
    return start_pos, end_pos, done_grid

def is_result(cur_pos, end_pos, cur_done_grid):
    if cur_pos == end_pos and all([cur_done_grid[i][j] for i in range(len(cur_done_grid)) for j in range(len(cur_done_grid[0]))]):
        return True
    return False

def get_next_states(cur_pos, cur_done_grid):
    next_states = []
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = (cur_pos[0]+dir[0], cur_pos[1]+dir[1])
        if x >=0 and x < len(cur_done_grid) and y >= 0 and y < len(cur_done_grid[0]) and cur_done_grid[x][y] == 0:
            next_states.append(((x, y), copy.deepcopy(cur_done_grid)))
    return next_states

def do(grid):
    start_pos, end_pos, init_done_grid = init(grid)
    stack = deque()
    stack.append((start_pos, init_done_grid))
    result = 0

    while len(stack) > 0:
        cur_pos, cur_done_grid = stack.pop()
        cur_done_grid[cur_pos[0]][cur_pos[1]] = 1
        if is_result(cur_pos, end_pos, cur_done_grid):
            result += 1
            continue
        for next_state in get_next_states(cur_pos, cur_done_grid):
            stack.append(next_state)
    return result
        


            
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return do(grid)

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
result = Solution().uniquePathsIII(grid)
assert result == 2

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,0,2]]
result = Solution().uniquePathsIII(grid)
assert result == 4

grid = [[0,1],
        [2,0]]
result = Solution().uniquePathsIII(grid)
assert result == 0
