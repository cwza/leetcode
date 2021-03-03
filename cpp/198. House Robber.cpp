#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i] = max(nums[i] + dp[i+2], dp[i+1])
dp[n] = 0
dp[n-1] = nums[n-1]
ans = dp[0]
*/

class Solution {
public:
    // int rob(vector<int>& nums) {
    //     int n = nums.size();
    //     if(n==0) return 0;
    //     int dp[n+1]; dp[n] = 0, dp[n-1] = nums[n-1];
    //     for(int i = n - 2; i >= 0; i--) {
    //         dp[i] = max(nums[i] + dp[i+2], dp[i+1]);
    //     }
    //     return dp[0];
    // }
    int rob(vector<int>& nums) {
        // 1D Space of above
        // Time: O(n), Space: O(1)
        int n = nums.size();
        if(n==0) return 0;
        int prev = 0, cur = nums[n-1];
        for(int i = n - 2; i >= 0; i--) {
            int cur_tmp = cur;
            cur = max(nums[i] + prev, cur);
            prev = cur_tmp;
        }
        return cur;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {1,2,3,1};
    ans = solution.rob(nums);
    assert(ans==4);

    solution = Solution();
    nums = {2,7,9,3,1};
    ans = solution.rob(nums);
    assert(ans==12);
}