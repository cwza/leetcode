#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// 2 pointer linklist cycle detection, Time: O(n), Space: O(1)
public:
    int findDuplicate(vector<int>& nums) {
        int head = nums[0];
        int slow = head, fast = head;
        while(true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow == fast) break;
        }
        slow = head;
        while(slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {1,3,4,2,2};
    ans = solution.findDuplicate(nums);
    assert(ans==2);

    solution = Solution();
    nums = {3,1,3,4,2};
    ans = solution.findDuplicate(nums);
    assert(ans==3);

    solution = Solution();
    nums = {1,1};
    ans = solution.findDuplicate(nums);
    assert(ans==1);

    solution = Solution();
    nums = {1,1,2};
    ans = solution.findDuplicate(nums);
    assert(ans==1);
}