#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i][j] = dp[i+1][j] or dp[i+1][j-nums[i]]
dp[n][j] = j == 0
dp[.][0] = true
ans = dp[0][target]
*/

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(1&sum) return false;
        int target = sum / 2;

        int n = nums.size();
        int dp[n+1][target+1];
        for(int i = n; i >= 0; i--) {
            for(int j = 0; j <= target; j++) {
                dp[i][j] = false;
                if(j == 0) dp[i][j] = true;
                else if(i == n) dp[i][j] = j == 0;
                else if(j-nums[i] >= 0) dp[i][j] = dp[i+1][j] || dp[i+1][j-nums[i]];
                else dp[i][j] = dp[i+1][j];
            }
        }
        return dp[0][target];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; bool ans;

    solution = Solution();
    nums = {1,5,11,5};
    ans = solution.canPartition(nums);
    assert(ans==true);

    solution = Solution();
    nums = {1,2,3,5};
    ans = solution.canPartition(nums);
    assert(ans==false);

    solution = Solution();
    nums = {14,9,8,4,3,2};
    ans = solution.canPartition(nums);
    assert(ans==true);
}