#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<string> vs;

class Solution {
public:
    vs ans;
    string mapping[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    void dfs(int i, string &path, string &digits) {
        if(i==digits.size()) {
            ans.push_back(path);
            return;
        }
        int digit = digits[i] - '0';
        for(char ch : mapping[digit]) {
            path.push_back(ch);
            dfs(i+1, path, digits);
            path.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        if(digits.size()==0) return ans;
        string path;
        dfs(0, path, digits);
        return ans;
    }
};

void printAns(vs ans) {
    for(auto str : ans) {
        cout << str << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string digits; vs ans;

    solution = Solution();
    digits = "23";
    ans = solution.letterCombinations(digits);
    printAns(ans);

    solution = Solution();
    digits = "";
    ans = solution.letterCombinations(digits);
    printAns(ans);

    solution = Solution();
    digits = "2";
    ans = solution.letterCombinations(digits);
    printAns(ans);
}