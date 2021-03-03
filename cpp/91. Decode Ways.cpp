#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i] = (dp[i+1] if s[i] in mapping else 0) + (dp[i+2] if s[i...i+1] in mapping else 0)
dp[n] = 1
dp[n-1] = 1 if 1<=s[n-1]<=9 else 0
ans = dp[0]
*/

class Solution {
public:
    // int numDecodings(string s) {
    //     // DP, Time: O(n), Space: O(n)
    //     int n = s.size();
    //     int dp[n+1]; fill(dp, dp+n+1, 0); 
    //     dp[n] = 1; 
    //     dp[n-1] = (s[n-1]-'0'>=1 && s[n-1]-'0'<=9) ? 1 : 0;
    //     for(int i = n-2; i >= 0; i--) {
    //         int num1 = s[i]-'0';
    //         if(num1>=1 && num1<=9) dp[i] += dp[i+1];
    //         int num2 = stoi(s.substr(i, 2));
    //         if(num2>=10 && num2<=26) dp[i] += dp[i+2];
    //     }
    //     return dp[0];
    // }
    int numDecodings(string s) {
        // DP, Time: O(n), Space: O(1)
        int n = s.size();
        int prevprev = 1; 
        int prev = (s[n-1]-'0'>=1 && s[n-1]-'0'<=9) ? 1 : 0;
        for(int i = n-2; i >= 0; i--) {
            int cur = 0;
            int num1 = s[i]-'0';
            if(num1>=1 && num1<=9) cur += prev;
            int num2 = stoi(s.substr(i, 2));
            if(num2>=10 && num2<=26) cur += prevprev;
            prevprev = prev;
            prev = cur;
        }
        return prev;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; int ans;

    solution = Solution();
    s = "12";
    ans = solution.numDecodings(s);
    assert(ans==2);

    solution = Solution();
    s = "226";
    ans = solution.numDecodings(s);
    assert(ans==3);

    solution = Solution();
    s = "0";
    ans = solution.numDecodings(s);
    assert(ans==0);
    
    solution = Solution();
    s = "1";
    ans = solution.numDecodings(s);
    assert(ans==1);
}