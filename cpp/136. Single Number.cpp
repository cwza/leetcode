#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// XOR Trick
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int num : nums) {
            ans ^= num;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {2,2,1};
    ans = solution.singleNumber(nums);
    assert(ans==1);

    solution = Solution();
    nums = {4,1,2,1,2};
    ans = solution.singleNumber(nums);
    assert(ans==4);

    solution = Solution();
    nums = {1};
    ans = solution.singleNumber(nums);
    assert(ans==1);
}