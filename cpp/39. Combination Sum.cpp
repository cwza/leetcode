#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vvi ans;
    void dfs(int i, int target, vi &path, vi &candidates) {
        int n = candidates.size();
        if(target == 0) {
            ans.push_back(path);
            return;
        }
        for(int j = i; j < n; j++) {
            int candidate = candidates[j];
            if(target-candidate < 0) continue;
            path.push_back(candidate);
            dfs(j, target-candidate, path, candidates);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vi path;
        dfs(0, target, path, candidates);
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

    Solution solution; vi candidates; int target; vvi ans;

    solution = Solution();
    candidates = {2,3,6,7};
    target = 7;
    ans = solution.combinationSum(candidates, target);
    printAns(ans);

    solution = Solution();
    candidates = {2,3,5};
    target = 8;
    ans = solution.combinationSum(candidates, target);
    printAns(ans);
}