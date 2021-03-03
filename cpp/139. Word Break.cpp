#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int > > vvi;
typedef pair<int, int> pi;

/*
dp[i]: True if s[i...n-1] is word breakable
dp[i] = any(s[i...j-1] in wordDict && dp[j] for j in [i+1, n])
dp[n] = true
ans = dp[0]
*/

class Solution {
// DP, Time: O(n^2), Space: O(n)
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());       
        int n = s.size();
        bool dp[n+1]; fill(dp, dp+n+1, false); dp[n] = true;
        for(int i = n-1; i >=0; i--) {
            for(int j = i+1; j <= n; j++) {
                string tmp = s.substr(i, j-i);
                if(dp[j] && dict.count(tmp)) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; vector<string> wordDict; bool ans;
    
    solution = Solution();
    s = "leetcode";
    wordDict = {"leet", "code"};
    ans = solution.wordBreak(s, wordDict);
    assert(ans==true);

    solution = Solution();
    s = "applepenapple";
    wordDict = {"apple", "pen"};
    ans = solution.wordBreak(s, wordDict);
    assert(ans==true);

    solution = Solution();
    s = "catsandog";
    wordDict = {"cats", "dog", "sand", "and", "cat"};
    ans = solution.wordBreak(s, wordDict);
    assert(ans==false);
}