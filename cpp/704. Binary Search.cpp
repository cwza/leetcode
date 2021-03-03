#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(logn), Space: O(1)
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while(l < r) {
            int m = l + (r-l)/2;
            if(nums[m] == target) return m;
            if(nums[m] > target) r = m;
            else l = m + 1;
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int target; int ans;

    solution = Solution();
    nums = {-1,0,3,5,9,12}, target = 9;
    ans = solution.search(nums, target);
    assert(ans==4);

    solution = Solution();
    nums = {-1,0,3,5,9,12}, target = 2;
    ans = solution.search(nums, target);
    assert(ans==-1);
}