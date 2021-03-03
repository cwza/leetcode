#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
/*
Just like 78 approach1, but
if we have duplicate elements (5, 5), instead of treating them as two elements that are duplicate, 
we can treat it as one special element 5, but this element has more than two choices: 
you can either NOT put it into the subset, 
or put ONE 5 into the subset, 
or put TWO 5s into the subset. 
Therefore, we are given an array (a1, a2, a3, ..., an) with each of them appearing (k1, k2, k3, ..., kn) times, the number of subset is (k1+1)(k2+1)...(kn+1). 
*/
public:
    vvi ans;
    void dfs(int i, vi &path, vi &nums, unordered_map<int, int> &counter) {
        int n = nums.size();
        if(i==n) {
            ans.push_back(path);
            return;
        }
        for(int count = 0; count <= counter[nums[i]]; count++){
            for(int _ = 0; _ < count; _++) path.push_back(nums[i]);
            dfs(i+1, path, nums, counter);
            for(int _ = 0; _ < count; _++) path.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        unordered_map<int, int> counter;
        for(auto num : nums) counter[num] += 1;
        nums = vi();
        for(auto [key, _] : counter) nums.push_back(key);

        vi path;
        dfs(0, path, nums, counter);
        return ans;
    }
};

// class Solution {
// // Just like 78 approach 2, but add sort and if cur num is equal to previous num skip it
// public:
//     vvi ans;
//     void dfs(int i, vi &path, vi &nums) {
//         int n = nums.size();
//         ans.push_back(path);
//         if(i==n) return;
//         unordered_set<int> checkDup;
//         for(int j = i; j < n; j++) {
//             if(checkDup.count(nums[j])) continue;
//             checkDup.insert(nums[j]);
//             path.push_back(nums[j]);
//             dfs(j+1, path, nums);
//             path.pop_back();
//         }
//     }
//     vector<vector<int>> subsetsWithDup(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         vi path;
//         dfs(0, path, nums);
//         return ans;
//     }
// };

void printAns(vvi ans) {
    for(auto l: ans) {
        cout << "(";
        for(auto n: l) {
            cout << n << " ";
        }
        cout << "), ";
    }
    cout << "\n";
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; vvi ans;

    solution = Solution();
    nums = {1,2,2};
    ans = solution.subsetsWithDup(nums);
    printAns(ans);

    solution = Solution();
    nums = {4,4,4,1,4};
    ans = solution.subsetsWithDup(nums);
    printAns(ans);
}