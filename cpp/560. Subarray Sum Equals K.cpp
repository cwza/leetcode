#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
k = 7
              0   1   2   3   4   5   6   7
nums=         3,  4,  7,  2, -3,  1,  4,  2
prefixsum=    3,  7, 14, 16, 13, 14, 18, 20
ans = [3, 4], [7], [7, 2, -3, 1], [1, 4, 2]

Where is [1, 4, 2] come from??
See that prefixsum[7]=20.
And we can find that 20-7=13 appeared at prefixsum[4].
That tell us 3+4+7+2-3+1+4+2=20 and 3+4+7+2-3=13
So 1+4+2=7
*/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> mp;
        mp[0] = 1;
        int prefix = 0;
        int ans = 0;
        for(int num : nums) {
            prefix += num;
            if(mp.count(prefix-k)) {
                ans += mp[prefix-k];
            }
            mp[prefix]++;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k, ans;

    nums = {1,1,1}, k = 2;
    ans = solution.subarraySum(nums, k);
    assert(ans==2);

    nums = {1,2,3}, k = 3;
    ans = solution.subarraySum(nums, k);
    assert(ans==2);
}