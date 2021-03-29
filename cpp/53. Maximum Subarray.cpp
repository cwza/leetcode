#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        ll prefixsum = 0; // sum in [0, i]
        ll curmin = 0; // min of all prefixsum in [0, 0], [0, 1], [0, 2],..., [0, i-1]
        // prefixsum - curmin = max subarray sum end at i
        ll ans = -1e18;
        for(int i = 0; i < n; ++i) {
            prefixsum += nums[i];
            ans = max(ans, prefixsum - curmin);
            curmin = min(curmin, prefixsum);
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