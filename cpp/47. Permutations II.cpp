#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
/*
Ex: [1, 1, 2]

    1     x     2
   . .         . .
  1   2       1   x
  .   .       .
  2   1       1

A key insight to avoid generating any redundant permutation is that at each step rather than viewing each number as a candidate, 
we consider each unique number as the true candidate. 
For instance, at the very beginning, given in the input of [1, 1, 2], we have only two true candidates instead of three.
*/
public:
    vvi ans;
    void dfs(int i, vi &path, unordered_set<int> &done, vi &nums) {
        int n = nums.size();
        if(i==n) {
            ans.push_back(path);
            return;
        }
        unordered_set<int> checkDup;
        for(int j = 0; j < n; j++) {
            if(done.count(j) || checkDup.count(nums[j])) continue;
            done.insert(j);
            checkDup.insert(nums[j]);
            path.push_back(nums[j]);
            dfs(i+1, path, done, nums);
            done.erase(j);
            path.pop_back();
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vi path;
        unordered_set<int> done;
        dfs(0, path, done, nums);
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
    nums = {1,1,2};
    ans = solution.permuteUnique(nums);
    printAns(ans);

    solution = Solution();
    nums = {1,2,3};
    ans = solution.permuteUnique(nums);
    printAns(ans);
}