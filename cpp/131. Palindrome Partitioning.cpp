#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<string> vs;
typedef vector<vector<string>> vvs;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;

// class Solution {
// public:
//     vvs ans;
//     vvb dp;
//     bool isPalindrone(int i, int j, string &s) {
//         string ori = s.substr(i, j-i+1);
//         string rev = string(ori);
//         reverse(rev.begin(), rev.end());
//         return ori == rev;
//     }
//     void dfs(int i, vs &path, string &s) {
//         int n = s.size();
//         if(i==n) {
//             ans.push_back(path);
//             return;
//         }
//         for(int j = i; j < n; j++) {
//             if(isPalindrone(i, j, s)) {
//                 path.push_back(s.substr(i, j-i+1));
//                 dfs(j+1, path, s);
//                 path.pop_back();
//             }
//         }
//     }
//     vector<vector<string>> partition(string s) {
//         vs path;
//         dfs(0, path, s);
//         return ans;
//     }
// };

class Solution {
/*
Dp on isPalindrone:
dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
dp[i][j] = true if j <= i
*/
public:
    vvs ans;
    vvb dp;
    bool isPalindrone(int i, int j, string &s, vvb &dp) {
        if(s[i] == s[j] &&(j-1 < i+1 || dp[i+1][j-1])) {
            dp[i][j] = true;
            return true;
        }
        return false;
    }
    void dfs(int i, vs &path, string &s, vvb &dp) {
        int n = s.size();
        if(i==n) {
            ans.push_back(path);
            return;
        }
        for(int j = i; j < n; j++) {
            if(isPalindrone(i, j, s, dp)) {
                path.push_back(s.substr(i, j-i+1));
                dfs(j+1, path, s, dp);
                path.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        int n = s.size();
        vvb dp(n, vb(n, false));
        vs path;
        dfs(0, path, s, dp);
        return ans;
    }
};

void printAns(vvs ans) {
    for(auto l : ans) {
        cout << "(";
        for(auto str : l) {
            cout << str << ", ";
        }
        cout << ") ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; vvs ans;

    solution = Solution();
    s = "aab";
    ans = solution.partition(s);   
    printAns(ans);

    solution = Solution();
    s = "a";
    ans = solution.partition(s);   
    printAns(ans);
}