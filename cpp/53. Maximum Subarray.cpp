#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    // int maxSubArray(vi& nums) {
    //     // Brute Force, Time: O(n^2), Space: O(1)
    //     int n = nums.size();
    //     int ans = INT_MIN;
    //     for(int i=0; i<n; i++) {
    //         int sum = 0;
    //         for(int j=i; j<n; j++) {
    //             sum += nums[j];
    //             ans = max(ans, sum);
    //         }
    //     }
    //     return ans;
    // }
    // int maxSubArray(vi& nums) {
    //     // DP, Time: O(n), Space: O(n)
    //     /*  dp[i]: max sum of sub-array from 0 to i include i
    //         dp[i] = max(dp[i-1]+nums[i], nums[i])
    //         dp[0] = nums[0] */
    //     int n = nums.size();
    //     int dp[n];
    //     dp[0] = nums[0];

    //     for(int i=1; i<n; i++) {
    //         dp[i] = max(dp[i-1]+nums[i], nums[i]);
    //     }

    //     return *max_element(dp, dp+n);
    // }
    int maxSubArray(vi& nums) {
        // DP, Time: O(n), Space: O(1)
        int n = nums.size();
        int sum = nums[0], ans = nums[0];
        for(int i=1; i<n; i++) {
            sum = max(sum+nums[i], nums[i]);
            ans = max(ans, sum);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {-2,1,-3,4,-1,2,1,-5,4};
    ans = solution.maxSubArray(nums);
    assert(ans==6);

    solution = Solution();
    nums = {1};
    ans = solution.maxSubArray(nums);
    assert(ans==1);

    solution = Solution();
    nums = {0};
    ans = solution.maxSubArray(nums);
    assert(ans==0);

    solution = Solution();
    nums = {-1};
    ans = solution.maxSubArray(nums);
    assert(ans==-1);

    solution = Solution();
    nums = {-2147483647};
    ans = solution.maxSubArray(nums);
    assert(ans==-2147483647);
}