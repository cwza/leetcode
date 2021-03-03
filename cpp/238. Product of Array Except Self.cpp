#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(n), Space: O(n)
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int left[n]; fill(left, left+n, 1);
        int right[n]; fill(right, right+n, 1);
        for(int i=0; i<=n-2; i++) {
            left[i+1] = left[i] * nums[i];
        }
        for(int i=n-1; i>=1; i--) {
            right[i-1] = right[i] * nums[i];
        }
        vi ans(n);
        for(int i=0; i<n; i++) {
            ans[i] = left[i] * right[i];
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution;
    vi nums = {1,2,3,4};
    vi ans = solution.productExceptSelf(nums);
    assert(ans==vi({24,12,8,6}));
}