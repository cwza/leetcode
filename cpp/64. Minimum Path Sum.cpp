#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// Push DP
// class Solution {
// public:
//     vector<vector<int>> dp;
//     int n, m;
//     int minPathSum(vector<vector<int>>& grid) {
//         int m = grid.size();
//         int n = grid[0].size();
//         dp = vector<vector<int>>(m, vector<int>(n, 1e9));
//         dp[0][0] = grid[0][0];
//         for(int i = 0; i < m; ++i) {
//             for(int j = 0; j < n; ++j) {
//                 if(j+1<n) dp[i][j+1] = min(dp[i][j+1], dp[i][j]+grid[i][j+1]);
//                 if(i+1<m) dp[i+1][j] = min(dp[i+1][j], dp[i][j]+grid[i+1][j]);
//             }
//         }
//         return dp[m-1][n-1];
//     }
// };

// Pull DP
class Solution {
public:
    vector<vector<int>> dp;
    int n, m;
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        dp = vector<vector<int>>(m, vector<int>(n, 1e9));
        dp[0][0] = grid[0][0];
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(i==0 && j==0) continue;
                if(i-1>=0) dp[i][j] = min(dp[i][j], dp[i-1][j]);
                if(j-1>=0) dp[i][j] = min(dp[i][j], dp[i][j-1]);
                dp[i][j] += grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi grid; int ans;

    solution = Solution();
    grid = {{1,3,1},{1,5,1},{4,2,1}};
    ans = solution.minPathSum(grid);
    assert(ans==7);

    solution = Solution();
    grid = {{1,2,3},{4,5,6}};
    ans = solution.minPathSum(grid);
    assert(ans==12);
}