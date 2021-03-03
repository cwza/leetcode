#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[i] = max(1+dp[j] for j in [i+1, n-1] if nums[i] < nums[j] else 1)
dp[n-1] = 1
ans = max(dp)
*/

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // DP, Time: O(n^2), Space: O(n)
        int n = nums.size();
        int dp[n]; fill(dp, dp+n, 1);
        for(int i = n-2; i >=0; i--) {
            for(int j = i+1; j < n; j++) {
                if(nums[i] < nums[j])
                    dp[i] = max(dp[i], 1+dp[j]);
            }
        }
        return *max_element(dp, dp+n);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {10,9,2,5,3,7,101,18};
    ans = solution.lengthOfLIS(nums);
    assert(ans==4);

    solution = Solution();
    nums = {0,1,0,3,2,3};
    ans = solution.lengthOfLIS(nums);
    assert(ans==4);

    solution = Solution();
    nums = {7,7,7,7,7,7,7};
    ans = solution.lengthOfLIS(nums);
    assert(ans==1);
}