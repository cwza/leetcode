#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Math, Time: O(n), Space: O(1)
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int expected = (0+n)*(n+1) / 2;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        return expected - sum;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {3,0,1};
    ans = solution.missingNumber(nums);
    assert(ans==2);

    solution = Solution();
    nums = {0,1};
    ans = solution.missingNumber(nums);
    assert(ans==2);

    solution = Solution();
    nums = {9,6,4,2,3,5,7,0,1};
    ans = solution.missingNumber(nums);
    assert(ans==8);
}