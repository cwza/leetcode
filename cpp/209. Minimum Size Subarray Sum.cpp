#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Sliding Window, Time: O(n), Space: O(1)
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        int l = 0;
        int total = 0;
        int ans = n+1;
        for(int r = 0; r < n; r++) {
            total += nums[r];
            while(total >= s) {
                ans = min(ans, r-l+1);
                total -= nums[l];
                l += 1;
            }
        }
        return ans==n+1 ? 0 : ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int s; vi nums; int ans;

    s = 7, nums = {2,3,1,2,4,3};
    ans = solution.minSubArrayLen(s, nums);
    assert(ans==2);
}