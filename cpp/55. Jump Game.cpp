#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// /*
// dp[i] = any(dp[j] for j in i+1...i+nums[i])
// dp[n-1] = true
// ans = dp[0]
// */
// public:
//     bool canJump(vector<int>& nums) {
//         // Time: O(n^2), Space: O(n)
//         int n = nums.size();
//         int dp[n]; fill(dp, dp+n, false); dp[n-1] = true;
//         for(int i = n-2; i >= 0; i--) {
//             for(int j = i+nums[i]; j > i; j--) {
//                 if(j<n && dp[j]) {
//                     dp[i] = true;
//                     break;
//                 }
//             }
//         }
//         return dp[0];
//     }
// };

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReachable = 0;
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            if(i>maxReachable) return false;
            maxReachable = max(maxReachable, i+nums[i]);
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; bool ans;

    solution = Solution();
    nums = {2,3,1,1,4};
    ans = solution.canJump(nums);
    assert(ans==true);

    solution = Solution();
    nums = {3,2,1,0,4};
    ans = solution.canJump(nums);
    assert(ans==false);

    solution = Solution();
    nums = {2, 0};
    ans = solution.canJump(nums);
    assert(ans==true);
}