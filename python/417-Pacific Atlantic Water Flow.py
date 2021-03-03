from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        "DFS, Time: O(mn), Space: O(mn)"
        if matrix == [] or matrix == [[]]: return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]
        def get_next_poses(cur_x, cur_y):
            nonlocal matrix
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            next_poses = []
            for dir in dirs:
                next_x, next_y = cur_x + dir[0], cur_y + dir[1]
                if 0<=next_x<m and 0<=next_y<n and matrix[next_x][next_y] >= matrix[cur_x][cur_y]:
                    next_poses.append((next_x, next_y))
            return next_poses
        def dfs(cur_x, cur_y, visited):
            if visited[cur_x][cur_y]: return
            visited[cur_x][cur_y] = True
            for next_x, next_y in get_next_poses(cur_x, cur_y):
                dfs(next_x, next_y, visited)
        for i in range(m):
            dfs(i, 0, pacific) # left
            dfs(i, n-1, atlantic) # right
        for j in range(n):
            dfs(0, j, pacific) # up
            dfs(m-1, j, atlantic) # down
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result

matrix = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]
result = Solution().pacificAtlantic(matrix)
assert result == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]