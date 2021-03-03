#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vvi ans;
    void dfs(int i, vi &path, int n, int k) {
        if(path.size() == k) {
            ans.push_back(path);
            return;
        }
        for(int j = i; j <= n; j++) {
            path.push_back(j);
            dfs(j+1, path, n, k);
            path.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vi path;
        dfs(1, path, n, k);
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

    Solution solution; int n, k; vvi ans;

    solution = Solution();
    n = 4, k = 2;
    ans = solution.combine(n, k);
    printAns(ans);

    solution = Solution();
    n = 1, k = 1;
    ans = solution.combine(n, k);
    printAns(ans);
}