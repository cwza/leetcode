#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Two pointers, Time: O(n^2), Space: O(1)
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        if(n < 3) return vvi();

        sort(nums.begin(), nums.end());
        vvi ans;
        for(int i = 0; i < n-2; i++) {
            if(i-1 >= 0 && nums[i] == nums[i-1]) continue; // skip duplicate num1
            int target = -nums[i];
            int l = i + 1, r = n-1;
            while(l < r) {
                if(nums[l] + nums[r] == target) {
                    ans.push_back(vi({nums[i], nums[l], nums[r]}));
                    while(l < r && nums[l+1] == nums[l]) l++; // Skip duplicate num2
                    while(l < r && nums[r-1] == nums[r]) r--; // Skip duplicate num3
                    l++; r--;
                }
                else if(nums[l] + nums[r] < target) l += 1;
                else if(nums[l] + nums[r] > target) r -= 1;
            }
        }
        return ans;
    }
};

#include <fmt/core.h>
#include <fmt/ranges.h>
using namespace fmt;
int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; vvi ans;

    nums = {-1,0,1,2,-1,-4};
    ans = solution.threeSum(nums);
    print("{}\n", ans);

    nums = {-2,0,0,2,2};
    ans = solution.threeSum(nums);
    print("{}\n", ans);
}