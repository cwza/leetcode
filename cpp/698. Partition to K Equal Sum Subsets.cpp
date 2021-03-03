#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// DFS
public:
    bool dfs(int i, vi &targets, vi nums, int k) {
        if(i == nums.size() && accumulate(targets.begin(), targets.end(), 0) == 0) return true;
        for(int j = 0; j < k; j++) {
            if(targets[j] >= nums[i]) {
                targets[j] -= nums[i];
                if(dfs(i+1, targets, nums, k)) return true;
                targets[j] += nums[i];
            } 
        }
        return false;
    }
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum % k != 0) return false;
        int target = sum / k;

        sort(nums.begin(), nums.end(), greater<int>());
        vi targets(k, target);
        return dfs(0, targets, nums, k);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k; bool ans;

    solution = Solution();
    nums = {4, 3, 2, 3, 5, 2, 1};
    k = 4;
    ans = solution.canPartitionKSubsets(nums, k);
    assert(ans==true);
}