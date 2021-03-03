#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(n), Space: O(n)
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> dupCheck;
        for(int num : nums) {
            if(dupCheck.count(num)) return true;
            dupCheck.insert(num);
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; bool ans;

    solution = Solution();
    nums = {1,2,3,1};
    ans = solution.containsDuplicate(nums);
    assert(ans==true);

    solution = Solution();
    nums = {1,2,3,4};
    ans = solution.containsDuplicate(nums);
    assert(ans==false);

    solution = Solution();
    nums = {1,1,1,3,3,4,3,2,4,2};
    ans = solution.containsDuplicate(nums);
    assert(ans==true);
}