from typing import List

class Move:
    def __init__(self):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        self.cur_dir_idx = 0
    def next_pos(self, pos):
        cur_dir = self.dirs[self.cur_dir_idx]
        return pos[0]+cur_dir[0], pos[1]+cur_dir[1]
    def next_dir(self):
        self.cur_dir_idx = (self.cur_dir_idx + 1) % 4
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        "Time: O(mn), Space: O(mn)"
        m = len(matrix)
        n = len(matrix[0])

        move = Move()
        done = set()
        cur_pos = (0, 0)
        result = []
        for _ in range(m*n):
            result.append(matrix[cur_pos[0]][cur_pos[1]])
            done.add(cur_pos)
            next_pos = move.next_pos(cur_pos)
            if (next_pos in done) or not (0<=next_pos[0]<m and 0<=next_pos[1]<n):
                move.next_dir()
                cur_pos = move.next_pos(cur_pos)
            else:
                cur_pos = next_pos
        return result

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
result = Solution().spiralOrder(matrix)
assert result == [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
result = Solution().spiralOrder(matrix)
assert result == [1,2,3,4,8,12,11,10,9,5,6,7]