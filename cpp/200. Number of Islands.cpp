#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<vector<char>> vvc;

class Solution {
public:
    int m;
    int n;
    bool isValid(int i, int j, vector<vector<char>> &grid) {
        return i>=0 && i<m && j>=0 && j<n && grid[i][j]=='1';
    }
    void dfs(int i, int j, vector<vector<char>> &grid) {
        grid[i][j] = '0';
        int xs[] = {1, -1, 0, 0};
        int ys[] = {0, 0, 1, -1};
        for(int k = 0; k < 4; ++k) {
            int ii = i + xs[k];
            int jj = j + ys[k];
            if(isValid(ii, jj, grid)) {
                dfs(ii, jj, grid);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();
        int ans = 0;
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(grid[i][j]=='1') {
                    ans++;
                    dfs(i, j, grid);
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