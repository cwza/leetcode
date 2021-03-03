#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Two Pointers, Time: O(n^2), Space: O(1)
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int diff = INT_MAX;
        int ans;
        for(int i = 0; i < n-2; i++) {
            int l = i + 1, r = n-1;
            while(l < r) {
                int s = nums[i] + nums[l] + nums[r];
                if(s == target) return s;
                if(abs(s-target) < diff) {
                    diff = abs(s-target);
                    ans = s;
                } else if(s < target) {
                    l++;
                } else if(s > target) {
                    r--;
                }
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution;
    vi nums = {-1,2,1,-4}; int target = 1;
    int ans = solution.threeSumClosest(nums, target);
    assert(ans==2);
}