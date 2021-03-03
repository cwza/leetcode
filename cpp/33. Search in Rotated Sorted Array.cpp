#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
Use the concept from LeetCode 153
if val < nums[0]: val is at Right hand side
else: val is at Left hand side

The different part of this problem is we can't use one g(m). We have 2 condition to consider:
1. If target is on the same side as nums[m], just run normal binary search
    nums[m] > target: search left, else search right
2. If target is on the different side of nums[m], 
    nums[m] is on the Right side: search left, else search right
*/

class Solution {
public:
    char getSide(vi &nums, int val) {
        // return 'R' if val is on the rhs else 'L' 
        if(val < nums[0]) return 'R';
        return 'L';
    }
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        char targetSide = getSide(nums, target);
        int l = 0, r = n;
        while(l < r) {
            int m = l + (r-l)/2;
            if(nums[m]==target) return m;
            char mSide = getSide(nums, nums[m]);
            if(mSide==targetSide) {
                if(nums[m] > target) r = m;
                else l = m + 1;
            } else {
                if(mSide=='R') r = m;
                else l = m + 1;
            }
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int target, ans;

    solution = Solution();
    nums = {4,5,6,7,0,1,2}, target = 0;
    ans = solution.search(nums, target);
    assert(ans==4);

    solution = Solution();
    nums = {4,5,6,7,0,1,2}, target = 3;
    ans = solution.search(nums, target);
    assert(ans==-1);

    solution = Solution();
    nums = {1}, target = 0;
    ans = solution.search(nums, target);
    assert(ans==-1);
}