#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(n), Space: O(1)
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vi ans;
        for(int num : nums) {
            num = abs(num);
            int idx = num - 1;
            if(nums[idx] < 0) ans.push_back(num);
            else {
                nums[idx] = -nums[idx]; 
            }
        }      
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution;
    vi nums = {4,3,2,7,8,2,3,1};
    vi ans = solution.findDuplicates(nums);
    assert(ans==vi({2, 3}));
}