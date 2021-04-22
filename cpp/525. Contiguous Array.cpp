#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

/*
Change num from 0 to -1.
Find the max contiguous subarray that sums up to 0.
Just like [CSES 1661 Subarray Sum II](https://cses.fi/problemset/task/1661/)
*/

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            if(nums[i]==0) nums[i] = -1;
        }
        map<int, int> mp;
        mp[0] = -1;
        int prefix = 0;
        int ans = 0;
        for(int i = 0; i < n; ++i) {
            prefix += nums[i];
            if(mp.count(prefix)) {
                ans = max(ans, i - mp[prefix]);
                mp[prefix] = min(mp[prefix], i);
            } else {
                mp[prefix] = i;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);

    vector<int> nums;
    Solution solution;
    nums = {0,0,1,0,0,0,1,1};
    cout << solution.findMaxLength(nums) << "\n";
}