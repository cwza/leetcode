#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
ans += right - left + 1....

For those who are confused, let's use the example nums = [10,5,2,6]:

If we start at the 0th index, [10], the number of intervals is obviously 1.
If we move to the 1st index, the window is now [10,5]. The new intervals created are [5] and [10,5], so we add 2.
Now, expand the window to the 2nd index: [10,5,2]. The new intervals are [2], [5,2], and [10,5,2], so we add 3.
The pattern should be obvious by now; we add right - left + 1 to the output variable every loop!
*/

class Solution {
// Sliding Window, Time: O(n), Space: O(1)
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if(k <= 1) return 0;
        int n = nums.size();       
        int l = 0;
        int product = 1, ans = 0;
        for(int r = 0; r < n; r++) {
            product *= nums[r];
            while(product >= k) {
                product /= nums[l];
                l += 1;
            }
            ans += r - l + 1;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution;
    vi nums = {10, 5, 2, 6}; int k = 100;
    int ans = solution.numSubarrayProductLessThanK(nums, k);
    assert(ans==8);
}