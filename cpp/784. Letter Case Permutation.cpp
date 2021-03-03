#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vector<string> ans;
    void dfs(int i, string path, string S) {
        if(i==S.size()) {
            ans.push_back(path);
            return;
        }
        if(isalpha(S[i])) {
            path.push_back(tolower(S[i]));
            dfs(i+1, path, S);
            path.pop_back();
            path.push_back(toupper(S[i]));
            dfs(i+1, path, S);
            path.pop_back();
        } else {
            path.push_back(S[i]);
            dfs(i+1, path, S);
            path.pop_back();
        }
    }
    vector<string> letterCasePermutation(string S) {
        dfs(0, "", S);
        return ans;
    }
};

void printAns(vector<string> ans) {
    for(auto str : ans) {
        cout << str << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string S; vector<string> ans;

    solution = Solution();
    S = "a1b2";
    ans = solution.letterCasePermutation(S);
    printAns(ans);   

    solution = Solution();
    S = "3z4";
    ans = solution.letterCasePermutation(S);
    printAns(ans);   

    solution = Solution();
    S = "12345";
    ans = solution.letterCasePermutation(S);
    printAns(ans);   

    solution = Solution();
    S = "0";
    ans = solution.letterCasePermutation(S);
    printAns(ans);   
}