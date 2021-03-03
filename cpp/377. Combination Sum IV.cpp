#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[x] = sum(dp[x-num] for num in nums)
dp[0] = 1
ans = dp[target]
*/

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        unsigned int dp[target+1]; fill(dp, dp+target+1, 0); dp[0] = 1;
        for(int x = 1; x <= target; ++x) {
            for(int num : nums) {
                if(x-num >= 0) dp[x] += dp[x-num];
            }
        }
        return dp[target];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int target; int ans;

    solution = Solution();
    nums = {1, 2, 3};
    target = 4;
    ans = solution.combinationSum4(nums, target);
    assert(ans==7);
}