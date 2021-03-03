#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
/* DFS 1:
        0              N
     .     .        .     .
    1       N      1       N
   . .     . .    . .     . .
  2   N   2   N  2   N   2   N
*/
public:
    vvi ans;
    void dfs(int i, vi &path, vi &nums) {
        if(i==nums.size()) {
            ans.push_back(path);
            return;
        }
        dfs(i+1, path, nums);
        path.push_back(nums[i]);
        dfs(i+1, path, nums);
        path.pop_back();
    }
    vvi subsets(vi& nums) {
        vi path;
        dfs(0, path, nums);
        return ans;
    }
};

class Solution {
/* DFS 2:
    0      1      2
  .   .    .  
 1     2   2
 .
 2
*/
public:
    vvi ans;
    void dfs(int i, vi &path, vi &nums) {
        int n = nums.size();
        ans.push_back(path);
        if(i==n) return;
        for(int j = i; j < n; j++) {
            path.push_back(nums[j]);
            dfs(j+1, path, nums);
            path.pop_back();
        }
    }
    vvi subsets(vi &nums) {
        vi path;
        dfs(0, path, nums);
        return ans;
    }
};

// class Solution {
// // Bit Manipulation
// public:
//     vvi subsets(vi& nums) {
//         int n = nums.size();
//         vvi ans;
//         for(int b = 0; b < 1<<n; b++) {
//             vi path;
//             for(int i = 0; i < n; i++) {
//                 if(b & 1<<i) path.push_back(nums[i]);
//             }
//             ans.push_back(path);
//         }
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
    nums = {1,2,3};
    ans = solution.subsets(nums);
    printAns(ans);

    solution = Solution();
    nums = {0};
    ans = solution.subsets(nums);
    printAns(ans);   
}