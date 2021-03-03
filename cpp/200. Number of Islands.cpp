#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<vector<char>> vvc;

class Solution {
public:
    void dfs(int x, int y, vvc &grid) {
        int m = grid.size(), n = grid[0].size();
        if(x<0 || x>=m || y<0 || y>=n || grid[x][y]=='0') return;
        grid[x][y] = '0';
        dfs(x, y+1, grid); dfs(x, y-1, grid); dfs(x+1, y, grid); dfs(x-1, y, grid);
    }
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int ans= 0;
        for(int x = 0; x < m; x++) {
            for(int y = 0; y < n; y++) {
                if(grid[x][y]=='1') {
                    ans++;
                    dfs(x, y, grid);
                }
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvc grid; int ans;

    solution = Solution();
    grid = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'}
    };
    ans = solution.numIslands(grid);
    assert(ans==1);

    solution = Solution();
    grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };
    ans = solution.numIslands(grid);
    assert(ans==3);
}