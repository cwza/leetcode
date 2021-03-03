from typing import List

'''
Algorithm for finding connected component in undirected graph using dfs
https://www.youtube.com/watch?v=9esCn0awd5k
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        "Find Connected Component in Undirected Graph, Time: O(mn), Space: O(1)"
        m = len(grid)
        n = len(grid[0])
        # for Space: O(1), we use the original grid as visited, "1": not visited, "0": visited
        def get_next_poses(cur_x, cur_y):
            nonlocal grid
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            next_poses = []
            for dir in dirs:
                next_x, next_y = cur_x + dir[0], cur_y + dir[1]
                if 0<=next_x<m and 0<=next_y<n and grid[next_x][next_y]=="1":
                    next_poses.append((next_x, next_y))
            return next_poses
        def dfs(cur_x, cur_y):
            grid[cur_x][cur_y] = "0"
            for next_x, next_y in get_next_poses(cur_x, cur_y):
                dfs(next_x, next_y)
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
result = Solution().numIslands(grid)
assert result == 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = Solution().numIslands(grid)
assert result == 3