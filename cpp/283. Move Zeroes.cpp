#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int ml0 = 0; // most left position of 0
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i]!=0) {
                swap(nums[ml0], nums[i]);
                ml0++;
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    vector<int> nums;
    Solution solution;
    nums = {0,1,0,3,12};
    solution.moveZeroes(nums);
    for(int a : nums) cout << a << " ";
    cout << "\n";
}