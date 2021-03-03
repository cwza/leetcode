#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
max_dp[i] = max(nums[i], nums[i]*max_dp[i+1], nums[i]*min_dp[i+1])
min_dp[i] = min(nums[i], nums[i]*max_dp[i+1], nums[i]*min_dp[i+1])
max_dp[n] = min_dp[n] = 1
ans = max(max_dp)
*/

class Solution {
public:
    // int maxProduct(vector<int>& nums) {
    //     // Time: O(n), Space: O(n)
    //     int n = nums.size();
    //     int maxDp[n+1]; maxDp[n] = 1;
    //     int minDp[n+1]; minDp[n] = 1;
    //     for(int i = n-1; i >= 0; i--) {
    //         int tmp[3] = {nums[i], nums[i]*maxDp[i+1], nums[i]*minDp[i+1]};
    //         maxDp[i] = *max_element(tmp, tmp+3);
    //         minDp[i] = *min_element(tmp, tmp+3);
    //     }
    //     return *max_element(maxDp, maxDp+n);
    // }
    int maxProduct(vector<int>& nums) {
        // Time: O(n), Space: O(1)
        int n = nums.size();
        int maxCur = 1, minCur = 1;
        int ans = INT_MIN;
        for(int i = n-1; i >= 0; i--) {
            int tmp[3] = {nums[i], nums[i]*maxCur, nums[i]*minCur};
            maxCur = *max_element(tmp, tmp+3);
            minCur = *min_element(tmp, tmp+3);
            ans = max(ans, maxCur);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {2,3,-2,4};
    ans = solution.maxProduct(nums);
    assert(ans==6);

    solution = Solution();
    nums = {-2,0,-1};
    ans = solution.maxProduct(nums);
    assert(ans==0);
}