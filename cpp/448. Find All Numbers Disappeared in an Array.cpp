#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// "Index trick, Time: O(2n), Space: O(1)"
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for(int num : nums) {
            num = abs(num);
            int idx = num - 1;
            nums[idx] = nums[idx]<0 ? nums[idx] : -nums[idx];
        }      
        vi ans;
        for(int i=0; i<nums.size(); i++) {
            if(nums[i]>=0) ans.push_back(i+1);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; vi ans;

    solution = Solution();
    nums = {4,3,2,7,8,2,3,1};
    ans = solution.findDisappearedNumbers(nums);
    assert(ans==vi({5,6}));
}