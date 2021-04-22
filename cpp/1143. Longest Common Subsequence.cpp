#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
    static const int maxN = 1000, maxM = 1000; 
    int n, m;
    int dp[maxN+1][maxM+1];
public:
    int longestCommonSubsequence(string text1, string text2) {
        n = text1.size();
        m = text2.size();
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                if(text1[i-1]==text2[j-1]) {
                    dp[i][j] = 1 + dp[i-1][j-1];
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
}