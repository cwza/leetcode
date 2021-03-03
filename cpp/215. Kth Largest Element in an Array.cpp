#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Quick Select by STL, Time: O(n), Space: O(1)
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        nth_element(nums.begin(), nums.begin()+n-k, nums.end());
        return nums[n-k];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k, ans;

    nums = {3,2,1,5,6,4}; k = 2;
    ans = solution.findKthLargest(nums, k);
    assert(ans==5);

    nums = {3,2,3,1,2,4,5,5,6}; k = 4;
    ans = solution.findKthLargest(nums, k);
    assert(ans==4);
}