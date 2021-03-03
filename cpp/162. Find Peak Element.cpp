#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();       
        int l = 0, r = n-1;
        while(l < r) {
            int m = l + (r-l)/2;
            if(nums[m+1] < nums[m]) r = m;
            else l = m+1;
        }
        return l;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {1,2,3,1};
    ans = solution.findPeakElement(nums);
    assert(ans==2);

    solution = Solution();
    nums = {1,2,1,3,5,6,4};
    ans = solution.findPeakElement(nums);
    assert(ans==5);
}