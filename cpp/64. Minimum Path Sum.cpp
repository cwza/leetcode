#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// DP, Time: O(nm), Space: O(nm)
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size()+1, n = grid[0].size()+1;
        int dp[m][n]; fill(&dp[0][0], &dp[0][0]+m*n, INT_MAX);

        for(int i=1; i<m; i++) {
            for(int j=1; j<n; j++) {
                if(i==1 && j==1) {
                    dp[i][j] = grid[i-1][j-1];
                } else {
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1];
                }
                // cout << dp[i][j] << " ";
            }
            // cout << endl;
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