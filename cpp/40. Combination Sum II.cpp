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
        unordered_set<int> checkDup;
        for(int j = i; j < n; j++) {
            int candidate = candidates[j];
            if(target-candidate < 0 || checkDup.count(candidate)) continue;
            checkDup.insert(candidate);
            path.push_back(candidate);
            dfs(j+1, target-candidate, path, candidates);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
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
    candidates = {10,1,2,7,6,1,5};
    target = 8;
    ans = solution.combinationSum2(candidates, target);
    printAns(ans);

    solution = Solution();
    candidates = {2,5,2,1,2};
    target = 5;
    ans = solution.combinationSum2(candidates, target);
    printAns(ans);
}