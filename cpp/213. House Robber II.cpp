#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

int helper(int start, int end, vector<int>& nums) {
    int n = end - start + 1;
    if(n==0) return 0;
    int prev = 0, cur = nums[end];
    for(int i = end - 1; i >= start; i--) {
        int cur_tmp = cur;
        cur = max(nums[i] + prev, cur);
        prev = cur_tmp;
    }
    return cur;
}

class Solution {
// Time: O(2n), Space: O(1)
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==1) return nums[0];
        return max(helper(1, n-1, nums), helper(0, n-2, nums));
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {2,3,2};
    ans = solution.rob(nums);
    assert(ans==3);

    solution = Solution();
    nums = {1,2,3,1};
    ans = solution.rob(nums);
    assert(ans==4);

    solution = Solution();
    nums = {0};
    ans = solution.rob(nums);
    assert(ans==0);
}