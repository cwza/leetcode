#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vector<string> ans;
    void dfs(int lCount, int rCount, string path, int n) {
        if(lCount == n && rCount == n) {
            ans.push_back(path);
            return;
        }
        if(lCount < n) {
            path.push_back('(');
            dfs(lCount+1, rCount, path, n);
            path.pop_back();
        }
        if(rCount < lCount) {
            path.push_back(')');
            dfs(lCount, rCount+1, path, n);
            path.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        dfs(0, 0, "", n);
        return ans;
    }
};

void printAns(vector<string> ans) {
    for(string str : ans) {
        cout << str << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int n; vector<string> ans;

    solution = Solution();
    n = 3;
    ans = solution.generateParenthesis(n);
    printAns(ans);

    solution = Solution();
    n = 1;
    ans = solution.generateParenthesis(n);
    printAns(ans);
}