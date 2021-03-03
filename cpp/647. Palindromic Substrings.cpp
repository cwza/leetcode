#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
dp[i][j] = true if j <= i
*/

class Solution {
public:
    int countSubstrings(string s) {
        // Time: O(n^2), Space: O(n^2)
        int n = s.size();
        bool dp[n][n]; fill(&dp[0][0], &dp[0][0]+n*n, false);      
        int ans = 0;
        for(int l = 1; l <= n; l++) {
            for(int i = 0; i <= n-l; i++) {
                int j = i + l - 1;
                if(l==1) dp[i][j] = true;
                else if(l==2) dp[i][j] = s[i]==s[j];
                else dp[i][j] = s[i]==s[j] && dp[i+1][j-1];
                if(dp[i][j]) ans++;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; int ans;

    solution = Solution();
    s = "abc";
    ans = solution.countSubstrings(s);
    assert(ans==3);

    solution = Solution();
    s = "aaa";
    ans = solution.countSubstrings(s);
    assert(ans==6);
}