#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;

class Solution {
// Brute Force + DP on isPalindrone, Time: O(n^2), Space: O(n^2)
/*
Dp on isPalindrone:
dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
dp[i][j] = true if j <= i
*/
public:
    bool isPalindrone(int i, int j, string &s, vvb &dp) {
        if(i==j) dp[i][j] = true;
        else if(j==i+1) dp[i][j] = s[i]==s[j];
        else dp[i][j] = s[i]==s[j] && dp[i+1][j-1];
        return dp[i][j];
    }
    string longestPalindrome(string s) {
        int n = s.size();
        vvb dp(n, vb(n, false));
        string ans = "";
        for(int l = 1; l <= n; l++) {
            for(int i = 0; i <= n-l ; i++) {
                int j = i + l - 1;
                if(isPalindrone(i, j, s, dp) && j-i+1 > ans.size()) {
                    ans = s.substr(i, j-i+1);
                }
            }
        }
        // for(int i = n-1; i >= 0; i--) {
        //     for(int j = i; j < n; j++) {
        //         if(isPalindrone(i, j, s, dp) && j-i+1 > ans.size()) {
        //             ans = s.substr(i, j-i+1);
        //         }
        //     }
        // }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; string ans;

    solution = Solution();
    s = "babad";
    ans = solution.longestPalindrome(s);
    assert(ans=="bab" || ans=="aba");

    solution = Solution();
    s = "cbbd";
    ans = solution.longestPalindrome(s);
    assert(ans=="bb");

    solution = Solution();
    s = "a";
    ans = solution.longestPalindrome(s);
    assert(ans=="a");

    solution = Solution();
    s = "ac";
    ans = solution.longestPalindrome(s);
    assert(ans=="a" || ans=="c");
}