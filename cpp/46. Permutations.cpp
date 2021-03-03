#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
/* DFS:
   0     1     2
  . .   . .   . .
  1 2   0 2   0 1
  . .   . .   . .
  2 1   2 0   1 0
*/
public:
    vvi ans;
    void dfs(int i, unordered_set<int> &done, vi &path, vi &nums) {
        int n = nums.size();
        if(i==n) {
            ans.push_back(path);
            return;
        }
        for(int j = 0; j < n; j++) {
            if(done.count(j)) continue;
            done.insert(j);
            path.push_back(nums[j]);
            dfs(i+1, done, path, nums);
            done.erase(j);
            path.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vi path;
        unordered_set<int> done;
        dfs(0, done, path, nums);
        return ans;
    }
};

class Solution {
// STL
public:
    vvi permute(vi& nums) {
        sort(nums.begin(), nums.end());
        vvi ans;
        do {
            ans.push_back(nums);
        } while(next_permutation(nums.begin(), nums.end()));
        return ans;
    }
};

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
    nums = {1, 2, 3};
    ans = solution.permute(nums);
    printAns(ans);

    solution = Solution();
    nums = {0, 1};
    ans = solution.permute(nums);
    printAns(ans);

    solution = Solution();
    nums = {1};
    ans = solution.permute(nums);
    printAns(ans);
}