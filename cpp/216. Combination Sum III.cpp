#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vvi ans;
    void dfs(int i, vi &path, int k, int target) {
        if(path.size() == k) {
            if(target == 0) ans.push_back(path);
            return;
        }
        for(int j = i; j <= 9; j++) {
            if(target-j < 0) continue;
            path.push_back(j);
            dfs(j+1, path, k, target-j);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vi path;
        dfs(1, path, k, n);
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

    Solution solution; int k, n; vvi ans;

    solution = Solution();
    k = 3, n = 7;
    ans = solution.combinationSum3(k, n);
    printAns(ans);

    solution = Solution();
    k = 3, n = 9;
    ans = solution.combinationSum3(k, n);
    printAns(ans);

    solution = Solution();
    k = 4, n = 1;
    ans = solution.combinationSum3(k, n);
    printAns(ans);

    solution = Solution();
    k = 3, n = 2;
    ans = solution.combinationSum3(k, n);
    printAns(ans);
}