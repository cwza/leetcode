#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// HashMap, Time: O(n), Space: O(n)
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> table; // val: index
        vi ans(2);
        for(int i=0; i<n; i++) {
            int num = nums[i];
            int remain = target - num;
            auto iter = table.find(remain);
            if(iter!=table.end()) {
                auto [val, idx] = *iter;
                ans[0] = idx;
                ans[1] = i;
            } else {
                table[num] = i;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int target; vi ans;

    solution = Solution();
    nums = {2,7,11,15}, target = 9;
    ans = solution.twoSum(nums, target);
    assert(ans==vi({0, 1}));

    solution = Solution();
    nums = {3,2,4}, target = 6;
    ans = solution.twoSum(nums, target);
    assert(ans==vi({1, 2}));
}