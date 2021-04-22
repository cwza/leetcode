#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

/*
https://www.youtube.com/watch?v=8uvWmiawJ8Q
dp[l][r] = cuts[r]-cuts[l] + min(dp[l][i]+dp[i][r] for i in [l+1, r-1])
Time Complexity: O(n^3), n is the length of cuts
Space Complexity: O(n^2), n is the length of cuts
*/

// Top-Down
// class Solution {
// public:
//     static const int maxC = 100;
//     int dp[maxC+2][maxC+2];
//     void dfs(int l, int r, vector<int> &cuts) {
//         if(r==l+1) {
//             dp[l][r] = 0;
//             return;
//         }
//         if(dp[l][r]!=-1) return;
//         dp[l][r] = 1e9;
//         for(int i = l + 1; i < r; ++i) {
//             dfs(l, i, cuts);
//             dfs(i, r, cuts);
//             dp[l][r] = min(dp[l][r], dp[l][i]+dp[i][r]);
//         }
//         dp[l][r] += cuts[r] - cuts[l];
//     }
//     int minCost(int n, vector<int>& cuts) {
//         cuts.push_back(0);
//         cuts.push_back(n);
//         sort(cuts.begin(), cuts.end());
//         int cn = cuts.size();
//         fill(&dp[0][0], &dp[0][0]+(maxC+2)*(maxC+2), -1);
//         dfs(0, cn-1, cuts);
//         return dp[0][cn-1];
//     }
// };


// Bottom-Up
class Solution {
public:
    static const int maxC = 100;
    int dp[maxC+2][maxC+2];
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        int cn = cuts.size();
        fill(&dp[0][0], &dp[0][0]+(maxC+2)*(maxC+2), -1);

        for(int r = 0; r < cn; ++r) {
            for(int l = r-1; l >= 0; --l) {
                if(r==l+1) {
                    dp[l][r] = 0;
                    continue;
                }
                dp[l][r] = 1e9;
                for(int i = r-1; i > l; --i) {
                    dp[l][r] = min(dp[l][r], dp[l][i]+dp[i][r]);
                }
                dp[l][r] += cuts[r] - cuts[l];
            }
        }
        return dp[0][cn-1];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    int n;
    vector<int> cuts;
    Solution solution;
    n = 7, cuts = {1,3,4,5};
    cout << solution.minCost(n, cuts) << endl;
    n = 9, cuts = {5,6,1,4,2};
    cout << solution.minCost(n, cuts) << endl;
}