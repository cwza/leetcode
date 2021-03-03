#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i][s]: the number of assignments which can lead to a sum of s from the ith index

dp[n][0] = 1
dp[n][else] = 0
dp[i][s] = dp[i+1][s-nums[i]] + dp[i+1][s+nums[i]]

ans = dp[0][S]
*/

class Solution {
public:
    // int findTargetSumWays(vector<int>& nums, int S) {
    //     // Bottom-Up DP on HashMap
    //     if(S > 1000 || S < -1000) return 0;
    //     int n = nums.size();
    //     vector<unordered_map<int, int>> dp(n+1);
    //     dp[n][0] = 1;

    //     for(int i = n-1; i >= 0; i--) {
    //         for(int s = -1000; s <= 1000; s++) {
    //             if(s-nums[i] >= -1000) dp[i][s] += dp[i+1][s-nums[i]];
    //             if(s+nums[i] <= 1000) dp[i][s] += dp[i+1][s+nums[i]];
    //         }
    //     }
    //     return dp[0][S];
    // }
    // int findTargetSumWays(vector<int>& nums, int S) {
    //     // Bottom-Up DP with shifted index on Array
    //     if(S > 1000 || S < -1000) return 0;
    //     int n = nums.size();
    //     int dp[n+1][2001]; fill(&dp[0][0], &dp[0][0]+(n+1)*2001, 0);
    //     // vvi dp(n+1, vi(2001, 0));
    //     dp[n][0+1000] = 1;

    //     for(int i = n-1; i >= 0; i--) {
    //         for(int s = -1000; s <= 1000; s++) {
    //             if(s-nums[i] >= -1000) dp[i][s+1000] += dp[i+1][s-nums[i]+1000];
    //             if(s+nums[i] <= 1000) dp[i][s+1000] += dp[i+1][s+nums[i]+1000];
    //         }
    //     }
    //     return dp[0][S+1000];
    // }
    int findTargetSumWays(vector<int>& nums, int S) {
        // 1D of above
        if(S > 1000 || S < -1000) return 0;
        int n = nums.size();
        int preDp[2001]={0}; 
        preDp[0+1000] = 1;
        int dp[2001]={0}; 

        for(int i = n-1; i >= 0; i--) {
            fill(dp, dp+2001, 0);
            for(int s = -1000; s <= 1000; s++) {
                if(s-nums[i] >= -1000) dp[s+1000] += preDp[s-nums[i]+1000];
                if(s+nums[i] <= 1000) dp[s+1000] += preDp[s+nums[i]+1000];
            }
            swap(preDp, dp);
        }
        return preDp[S+1000];
    }
};

// class Solution {
// // Top-Down with Memoization
// public:
//     int dfs(int i, int s, unordered_map<string, int> &memo, vi &nums) {
//         int n = nums.size();
//         if(s > 1000 || s < -1000) return 0;
//         if(i==n && s==0) return 1;
//         if(i==n) return 0;
//         string key = to_string(i) + "," + to_string(s);
//         if(memo.count(key)) return memo[key];

//         int res = dfs(i+1, s-nums[i], memo, nums) + dfs(i+1, s+nums[i], memo, nums);
//         memo[key] = res;
//         return res;
//     }
//     int findTargetSumWays(vector<int>& nums, int S) {
//         unordered_map<string, int> memo;
//         return dfs(0, S, memo, nums);
//     }
// };

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int S; int ans;

    solution = Solution();
    nums = {1, 1, 1, 1, 1};
    S = 3;
    ans = solution.findTargetSumWays(nums, S);
    // cout << ans;
    assert(ans==5);
}