#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    int maxNonOverlapping(vector<int>& nums, int target) {
        set<int> s;
        s.insert(0);
        ll prefix = 0, ans = 0;
        for(int a : nums) {
            prefix += a;
            auto iter = s.find(prefix-target);
            if(iter!=s.end()) {
                ans++;
                s.clear();
            }
            s.insert(prefix);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);

    vector<int> nums;
    int target;
    Solution solution;

    nums = {1,1,1,1,1}, target = 2;
    cout << solution.maxNonOverlapping(nums, target) << endl;
    nums = {-1,3,5,1,4,2,-9}, target = 6;
    cout << solution.maxNonOverlapping(nums, target) << endl;
    nums = {-2,6,6,3,5,4,1,2,8}, target = 10;
    cout << solution.maxNonOverlapping(nums, target) << endl;
    nums = {0,0,0}, target = 0;
    cout << solution.maxNonOverlapping(nums, target) << endl;
}