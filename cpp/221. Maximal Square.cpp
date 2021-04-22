#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

// https://www.youtube.com/watch?v=oPrpoVdRLtg

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int ans = 0;
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(i==0 || j==0) {
                    if(matrix[i][j]=='1') dp[i][j] = 1;
                } else if(matrix[i][j]=='1') {
                    dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
                }
                ans = max(ans, dp[i][j]*dp[i][j]);
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
}