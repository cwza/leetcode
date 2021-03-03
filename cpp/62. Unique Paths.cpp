#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[x][y] = dp[x+1][y] + dp[x][y+1]
dp[m-1][n-1] = 1
ans = dp[0][0]
*/

class Solution {
public:
    // int uniquePaths(int m, int n) {
    //     // DP, Time: O(n^2), Space: O(n^2)
    //     int dp[m][n]; fill(&dp[0][0], &dp[0][0]+m*n, 0); dp[m-1][n-1] = 1;
    //     for(int x = m-1; x >= 0; x--) {
    //         for(int y = n-1; y >= 0; y--) {
    //             if(x==m-1 && y==n-1) continue;
    //             if(x+1>=0 && x+1<m) dp[x][y] += dp[x+1][y];
    //             if(y+1>=0 && y+1<n) dp[x][y] += dp[x][y+1];
    //         }
    //     }
    //     return dp[0][0];
    // }
    int uniquePaths(int m, int n) {
        // DP, Time: O(n^2), Space: O(n)
        int dp[n]; fill(dp, dp+n, 0); dp[n-1] = 1;
        for(int x = m-1; x >= 0; x--) {
            for(int y = n-1; y >= 0; y--) {
                // if(x+1>=0 && x+1<m) dp[x][y] += dp[x+1][y];
                // if(y+1>=0 && y+1<n) dp[x][y] += dp[x][y+1];
                if(x==m-1 && y==n-1) continue;
                if(y+1>=0 && y+1<n) dp[y] = dp[y] + dp[y+1];
            }
        }
        return dp[0];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int m, n, ans;   

    solution = Solution();
    m = 3, n = 7;
    ans = solution.uniquePaths(m, n);
    assert(ans==28);

    solution = Solution();
    m = 3, n = 2;
    ans = solution.uniquePaths(m, n);
    assert(ans==3);

    solution = Solution();
    m = 7, n = 3;
    ans = solution.uniquePaths(m, n);
    assert(ans==28);

    solution = Solution();
    m = 3, n = 3;
    ans = solution.uniquePaths(m, n);
    assert(ans==6);
}