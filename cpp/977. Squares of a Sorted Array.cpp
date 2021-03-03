#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// 2 Pointers, Time: O(n), Space: O(n)
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l=0, r=nums.size()-1;      
        vi ans(nums.size());
        int i = r;
        while(l<=r) {
            if(abs(nums[l]) >= abs(nums[r])) {
                ans[i] = pow(nums[l], 2);
                l += 1;
                i -= 1;
            } else {
                ans[i] = pow(nums[r], 2);
                r -= 1;
                i -= 1;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; vi ans;

    solution = Solution();
    nums = {-4,-1,0,3,10};
    ans = solution.sortedSquares(nums);
    assert(ans==vi({0,1,9,16,100}));

    solution = Solution();
    nums = {-7,-3,2,3,11};
    ans = solution.sortedSquares(nums);
    assert(ans==vi({4,9,9,49,121}));

}